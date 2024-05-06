
/*========================== INSERTS =============================*/

INSERT INTO tipo_venta (id, nombre, descripcion)
VALUES 
(1, 'Venta al contado', 'La venta se paga al contado'),
(2, 'Venta a credito', 'Se genera los pagos en cuotas de la venta');

INSERT INTO piso (id, nombre)
VALUES 
(1, 'Planta baja'),
(2, 'Planta alta');

INSERT INTO sector (nombre) VALUES 
('Cárnicos'),
('Abarrotes'),
('Frutas'),
('Ferreterías'),
('Cosméticos'),
('Panadería'),
('Lácteos'),
('Librerías'),
('Ropas'),
('Zapatos'),
('Sastrería'),
('Otros');

INSERT INTO rol (id, nombre, descripcion) VALUES
(1, 'Administrador', 'Rol con acceso total al sistema.'),
(2, 'Encargado_ventas', 'Rol con permisos de Encargado ventas.');

INSERT INTO persona (nombres, p_apellido, s_apellido, nro_ci, telefono, direccion) VALUES 
('Juan', 'Pérez', 'García', '1234567', '123456789', 'Calle 123, Ciudad'),
('María', 'López', 'Martínez', '2345678', '234567890', 'Avenida Principal, Pueblo'),
('Pedro', 'Gómez', 'Fernández', '3456789', '345678901', 'Calle Central, Villa'),
('Ana', 'Rodríguez', 'Sánchez', '4567890', '456789012', 'Boulevard, Aldea'),
('Luis', 'Martínez', 'Díaz', '5678901', '567890123', 'Carrera 45, Municipio'),
-- cliente
('Laura', 'Sánchez', 'Gómez', '1112223', '678901234', 'Camino 67, Caserío'),
('Carlos', 'García', 'López', '2223334', '789012345', 'Paseo 89, Poblado'),
('Sofía', 'Fernández', 'Martínez', '4445556', '890123456', 'Travesía 12, Alquería'),
('Diego', 'Díaz', 'Rodríguez', '6667778', '901234567', 'Callejón 56, Barrio'),
('Julia', 'Gómez', 'Pérez', '8889991', '012345678', 'Plaza Mayor, Sector');

INSERT INTO personal (id, estado) VALUES 
(1, 'A'),
(2, 'A'),
(3, 'A'),
(4, 'A'),
(5, 'I');

INSERT INTO usuario (usuario, password, estado, id_personal, id_rol) 
VALUES 
('admin1', md5('1234'), 'A', 1, 1),
('enventa1', md5('1234'), 'A', 2, 2),
('enventa2', md5('1234'), 'A', 3, 2),
('enventa3', md5('1234'), 'A', 4, 2),
('enventa4', md5('1234'), 'I', 5, 2);

INSERT INTO encargado_ventas (id, observacion) VALUES 
(1, 'es admin'),
(2, 'es un encargado'),
(3, 'es un encargado'),
(4, 'es un encargado'),
(5, 'es un encargado');

INSERT INTO cliente (id, observacion) VALUES 
(6, 'es un cliente'),
(7, 'es un cliente'),
(8, 'es un cliente'),
(9, 'es un cliente'),
(10, 'es un cliente');

INSERT INTO pasillo (nombre, id_piso) VALUES 
('Pasillo 1', 1),
('Pasillo 2', 1),
('Pasillo 3', 1),

('Pasillo 1', 2),
('Pasillo 2', 2),
('Pasillo 3', 2);

INSERT INTO local_comercial (nro_local, precio, metros_cuadrados, descripcion, estado, id_sector, id_pasillo) VALUES 
('A-1', 20000.00, 10.00, 'Local descripcion 1', 'D', 1, 1),
('A-2', 23000.00, 15.00, 'Local descripcion 2', 'D', 1, 2),
('A-3', 20000.00, 10.00, 'Local descripcion 3', 'O', 2, 1),
('A-4', 23000.00, 15.00, 'Local descripcion 4', 'D', 2, 2),
('A-5', 20000.00, 10.00, 'Local descripcion 5', 'D', 3, 1),
('A-6', 20000.00, 10.00, 'Local descripcion 6', 'O', 3, 2);






