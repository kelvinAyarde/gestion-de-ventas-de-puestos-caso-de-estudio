
/*========================== PROCEDIMIENTOS ==============================*/

-- verificar credenciales de usuario
DELIMITER //
CREATE PROCEDURE verificar_credencial(
    IN p_usuario VARCHAR(50),
    IN p_password VARCHAR(128)
)
BEGIN	
	SELECT p.id as id_personal, r.id as id_rol, pe.nombres, pe.p_apellido, pe.s_apellido, u.usuario as usuario, r.nombre as rol
    FROM personal p
    JOIN usuario u ON p.id = u.id_personal
    JOIN rol r ON u.id_rol = r.id
    JOIN persona pe ON pe.id = p.id
    WHERE u.usuario = p_usuario AND u.password = md5(p_password)
    AND u.estado = 'A' AND p.estado = 'A';
END //
DELIMITER ;

-- registro_credito_generar_cuota
DELIMITER //
CREATE PROCEDURE registro_credito_generar_cuota(
    IN p_cantidad_cuotas INT,
    IN p_monto NUMERIC(10, 2),
    IN p_fecha_inicio DATE,
    IN p_tasa_interes_anual NUMERIC(5, 2),
    IN p_id_venta INT
)
BEGIN
    DECLARE monto_cuota NUMERIC(10, 2);
    DECLARE saldo_pendiente NUMERIC(10, 2);
    DECLARE tasa_interes_mensual NUMERIC(5, 2);
    DECLARE i INT DEFAULT 1;
	DECLARE p_fecha_fin DATE;
	
	-- calcular la fecha_fin de pagos del credito
	set p_fecha_fin =  DATE_ADD(p_fecha_inicio, INTERVAL (p_cantidad_cuotas - 1) MONTH);
    -- Insertar datos del crédito
    INSERT INTO credito (cantidad_cuotas, monto, fecha_registro, fecha_inicio, fecha_fin, estado, tasa_interes_anual, id_venta) 
    VALUES (p_cantidad_cuotas, p_monto, NOW(), p_fecha_inicio, p_fecha_fin, 'P', p_tasa_interes_anual, p_id_venta);

    -- Obtener el ID del último crédito insertado
    SET @credito_id = LAST_INSERT_ID();

    -- Calcular tasa de interés mensual
    SET tasa_interes_mensual = p_tasa_interes_anual / 12 / 100;

    -- Calcular monto de la cuota
    SET monto_cuota = p_monto * (tasa_interes_mensual * POWER(1 + tasa_interes_mensual, p_cantidad_cuotas)) / (POWER(1 + tasa_interes_mensual, p_cantidad_cuotas) - 1);

    -- Insertar cuotas
    SET saldo_pendiente = p_monto;
    WHILE i <= p_cantidad_cuotas DO
        INSERT INTO cuota (nro_cuota, fecha_pago, estado, monto_capital, monto_interes, monto_mora, id_credito)
        VALUES (i, DATE_ADD(p_fecha_inicio, INTERVAL (i - 1) MONTH), 'P', monto_cuota - (saldo_pendiente * tasa_interes_mensual), saldo_pendiente * tasa_interes_mensual, 0, @credito_id);
        
        SET saldo_pendiente = saldo_pendiente - (monto_cuota - (saldo_pendiente * tasa_interes_mensual));
        SET i = i + 1;
    END WHILE;
END//
DELIMITER ;

/*===================== TRIGGERS ==========================*/

-- Actualizar el estado de un local comercial al registrar una venta
DELIMITER //
CREATE TRIGGER reg_venta_actualizar_local_comercial
AFTER INSERT ON venta
FOR EACH ROW
BEGIN
    UPDATE local_comercial
    SET estado = 'O'
    WHERE id_sector = NEW.id_sector AND id_pasillo = NEW.id_pasillo;
END//
DELIMITER ;

-- reg_pago_contado_actualizar_venta
DELIMITER //
CREATE TRIGGER reg_pago_contado_actualizar_venta
AFTER INSERT ON pago_contado
FOR EACH ROW
BEGIN
    UPDATE venta
    SET estado = 'R'
    WHERE id = NEW.id_venta;
END//
DELIMITER ;

-- reg_pago_cuota_actualizar_cuota
DELIMITER //
CREATE TRIGGER reg_pago_cuota_actualizar_cuota
AFTER INSERT ON pago_cuota
FOR EACH ROW
BEGIN
    UPDATE cuota
    SET estado = 'R'
    WHERE id = NEW.id_cuota;
END//
DELIMITER ;

-- reg_pago_cuota_fin_cuota
DELIMITER //
CREATE TRIGGER reg_pago_cuota_fin_cuota
AFTER INSERT ON pago_cuota
FOR EACH ROW
BEGIN
    DECLARE p_id_credito INT;
    DECLARE total_pagos_cuotas BOOLEAN;
	DECLARE p_id_venta INT;
    -- Obtener el ID del crédito asociado a la cuota insertada
    SELECT id_credito INTO p_id_credito FROM cuota WHERE id = NEW.id_cuota;

    -- Verificar si todas las cuotas asociadas al crédito están en estado 'R'
    SELECT COUNT(*) = SUM(CASE WHEN estado = 'R' THEN 1 ELSE 0 END)
    INTO total_pagos_cuotas
    FROM cuota
    WHERE id_credito = p_id_credito;

    -- Si todas las cuotas están en estado 'R', actualizar el estado del crédito a 'R'
    IF total_pagos_cuotas THEN
        UPDATE credito
        SET estado = 'R'
        WHERE id = p_id_credito;

        -- Obtener el ID de la venta asociada al crédito
        SELECT id_venta INTO p_id_venta FROM credito WHERE id = p_id_credito;

        -- Actualizar el estado de la venta a 'R'
        UPDATE venta
        SET estado = 'R'
        WHERE id = p_id_venta;
    END IF;
END //
DELIMITER ;

/*
-- otra forma de hacer el reg_pago_cuota_fin_cuota
DELIMITER //
CREATE TRIGGER reg_pago_cuota_fin_cuota
AFTER INSERT ON pago_cuota
FOR EACH ROW
BEGIN
    -- Obtener el ID del crédito asociado a la cuota insertada
    DECLARE p_id_credito INT;
    SELECT id_credito INTO p_id_credito FROM cuota WHERE id = NEW.id_cuota;

    -- Verificar si todas las cuotas asociadas al crédito están en estado 'R'
    IF (
        SELECT COUNT(*) = SUM(CASE WHEN estado = 'R' THEN 1 ELSE 0 END)
        FROM cuota
        WHERE id_credito = p_id_credito
    ) THEN
        -- Actualizar el estado del crédito a 'R'
        UPDATE credito
        SET estado = 'R'
        WHERE id = p_id_credito;

        -- Actualizar el estado de la venta asociada al crédito a 'R'
        UPDATE venta
        SET estado = 'R'
        WHERE id = (
            SELECT id_venta
            FROM credito
            WHERE id = p_id_credito
        );
    END IF;
END //
DELIMITER ;
*/








