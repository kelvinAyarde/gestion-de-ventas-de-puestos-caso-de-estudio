

CREATE TABLE persona(
    id int NOT null auto_increment,
    nombres varchar(50) not null,
	p_apellido varchar(50) not null,
	s_apellido varchar(50),
    nro_ci varchar(15) not null unique,
	telefono varchar(15) not null,
	direccion varchar(250),
    PRIMARY KEY(id)
)engine=innodb;

CREATE TABLE personal (
    id INT NOT NULL PRIMARY KEY,
	estado char(1) not null CHECK (estado IN ('A', 'I')),
    FOREIGN KEY (id) REFERENCES persona(id)
) ENGINE=InnoDB;

CREATE TABLE rol(
    id INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(250) NOT NULL,
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE usuario(
    id int NOT null auto_increment,
    usuario varchar(50) not null UNIQUE,
    password varchar(130) not null,
    estado char(1) not null CHECK (estado IN ('A','I')),
    id_personal int not null,
    id_rol int not null,
    foreign key (id_personal) references personal(id),
    foreign key (id_rol) references rol(id),
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE encargado_ventas (
    id INT NOT NULL PRIMARY KEY,
	observacion varchar(250),
    FOREIGN KEY (id) REFERENCES personal(id)
) ENGINE=InnoDB;

CREATE TABLE cliente (
    id INT NOT NULL PRIMARY KEY,
	observacion varchar(250),
    FOREIGN KEY (id) REFERENCES persona(id)
) ENGINE=InnoDB;

/*============== Parte fisica de LOCAL COMERCIAL ==============*/
CREATE TABLE piso(
    id INT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE sector(
    id INT NOT NULL auto_increment,
    nombre VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE pasillo(
    id INT NOT NULL auto_increment,
    nombre VARCHAR(30) NOT NULL,
	id_piso INT NOT NULL,
	FOREIGN KEY (id_piso) REFERENCES piso(id),
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE local_comercial(
    nro_local VARCHAR(20) NOT NULL,
	precio NUMERIC(10, 2) NOT NULL,
	metros_cuadrados DECIMAL(10,2) NOT NULL,
	descripcion VARCHAR(250),
	estado char(1) not null CHECK (estado IN ('O','D','I')),
	id_sector INT NOT NULL,
	id_pasillo INT NOT NULL,
	FOREIGN KEY (id_sector) REFERENCES sector(id),
	FOREIGN KEY (id_pasillo) REFERENCES pasillo(id),
    PRIMARY KEY(id_sector,id_pasillo)
)engine = innodb;

/*=================================================================*/

CREATE TABLE tipo_venta(
    id INT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
	descripcion VARCHAR(250) NOT NULL,
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE venta(
    id INT NOT NULL auto_increment,
    fecha_registro datetime NOT NULL,
	precio_venta NUMERIC(10, 2) NOT NULL,
	estado char(1) not null CHECK (estado IN ('P','R','A')),
	id_cliente INT NOT NULL,
	id_tipo_venta INT NOT NULL,
	id_encargado_ventas INT NOT NULL,	
	id_sector INT NOT NULL,
	id_pasillo INT NOT NULL,
	FOREIGN KEY (id_cliente) REFERENCES cliente(id),
	FOREIGN KEY (id_tipo_venta) REFERENCES tipo_venta(id),
	FOREIGN KEY (id_encargado_ventas) REFERENCES encargado_ventas(id),
	FOREIGN KEY (id_sector, id_pasillo) REFERENCES local_comercial(id_sector, id_pasillo),
    PRIMARY KEY(id)
)engine = innodb;

/*=================== casos de venta al contado, credito, credito revertido ===================*/

CREATE TABLE local_comercial_revertido(
    id INT NOT NULL auto_increment,
	fecha_reversion datetime NOT NULL,
	motivo_reversion VARCHAR(250) NOT NULL,	
	id_venta INT NOT NULL,
	FOREIGN KEY (id_venta) REFERENCES venta(id),
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE pago_contado(
    id INT NOT NULL auto_increment,
	fecha_registro datetime NOT NULL,
	monto NUMERIC(10, 2) NOT NULL,
	observacion VARCHAR(250),	
	id_venta INT NOT NULL,
	FOREIGN KEY (id_venta) REFERENCES venta(id),
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE credito(
    id INT NOT NULL auto_increment,
	cantidad_cuotas INT NOT NULL,
	monto NUMERIC(10, 2) NOT NULL,
	fecha_registro datetime NOT NULL,
	fecha_inicio date NOT NULL,
	fecha_fin date NOT NULL,
	estado char(1) not null CHECK (estado IN ('P','R','A')),	
	tasa_interes_anual NUMERIC(5, 2) not null,
	id_venta INT NOT NULL,
	FOREIGN KEY (id_venta) REFERENCES venta(id),
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE cuota(
    id INT NOT NULL auto_increment,
	nro_cuota INT NOT NULL,
	fecha_pago date NOT NULL,
	estado char(1) not null CHECK (estado IN ('P','R','A')),	
	monto_capital NUMERIC(10, 2) NOT NULL,
	monto_interes NUMERIC(10, 2) NOT NULL,
	monto_mora NUMERIC(10, 2) NOT NULL,
	id_credito INT NOT NULL,
	FOREIGN KEY (id_credito) REFERENCES credito(id),
    PRIMARY KEY(id)
)engine = innodb;

CREATE TABLE pago_cuota(
    id INT NOT NULL auto_increment,
	fecha_registro datetime NOT NULL,
	monto NUMERIC(10, 2) NOT NULL,
	observacion VARCHAR(250),	
	id_cuota INT NOT NULL,
	FOREIGN KEY (id_cuota) REFERENCES cuota(id),
    PRIMARY KEY(id)
)engine = innodb;















