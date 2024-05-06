
-- buscar cliente y verificar si tiene pagos pendientes
SELECT cl.id as id_cliente, CONCAT(p.nombres,' ',p.p_apellido) as nombre,
	CASE
		WHEN v.estado = 'P' THEN 'S'
		ELSE 'N'
	END AS pago_pendiente
FROM cliente cl JOIN persona p ON p.id = cl.id
LEFT JOIN venta v ON v.id_cliente = cl.id
WHERE p.nro_ci = '7890123';

-- traer local_comercial
SELECT lc.id_sector, lc.id_pasillo , lc.nro_local , lc.precio, lc.metros_cuadrados, lc.descripcion, lc.estado,
	s.nombre as sector, p.nombre as pasillo, pi.nombre as piso
FROM local_comercial lc 
JOIN sector s ON lc.id_sector = s.id
JOIN pasillo p ON lc.id_pasillo = p.id
JOIN piso pi ON p.id_piso = pi.id;

-- traer las configuraciones de tipo de venta 
SELECT tv.id, tv.nombre FROM tipo_venta tv;


/*-------------------------- AUN NO PROBADO --------------------------*/
-- obtener pago de venta al contado
SELECT v.id, v.fecha_registro, v.precio_venta, lc.nro_local, CONCAT(p.nombres,' ',p.p_apellido) as nombre_cliente
FROM venta v
JOIN cliente cl ON v.id_cliente = cl.id
JOIN persona p ON p.id = cl.id
JOIN local_comercial lc ON lc.id_sector = v.id_sector AND lc.id_pasillo = v.id_pasillo
WHERE v.estado='P' AND v.id_tipo_venta = 1 AND p.nro_ci = '6789012';

-- obtener pago de venta al credito
SELECT v.id, v.fecha_registro, v.precio_venta, lc.nro_local, CONCAT(p.nombres,' ',p.p_apellido) as nombre_cliente
FROM venta v
JOIN cliente cl ON v.id_cliente = cl.id
JOIN persona p ON p.id = cl.id
JOIN local_comercial lc ON lc.id_sector = v.id_sector AND lc.id_pasillo = v.id_pasillo
WHERE v.estado='P' AND v.id_tipo_venta = 2 AND p.nro_ci = '7890123';

-- obtener cuotas del credito de la venta por el id_venta y verificar si la cuota es valida para pagar
SELECT cu.id, cu.nro_cuota, cu.fecha_pago, cu.estado , cu.monto_capital, cu.monto_interes,cu.monto_mora,
	CASE
        WHEN cu.estado = 'P' AND ant.estado = 'P' THEN 'S'
        ELSE 'N'
    END AS pagar_cuota_anterior
FROM credito cr 
JOIN venta v ON v.id = cr.id_venta
JOIN cuota cu ON cu.id_credito = cr.id
LEFT JOIN cuota ant ON cu.id_credito = ant.id_credito AND cu.nro_cuota = ant.nro_cuota + 1
WHERE v.id = 5 AND cu.estado= 'P'
ORDER BY cu.nro_cuota;

