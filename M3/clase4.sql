use adventureworks;

create database henry_01;
use henry_01;
show tables;
create table gasto (
	idGasto int,
    idSucursal int,
    idTipoGasto int,
    fecha date,
    monto decimal(10,2)
);

set global local_infile = on;

show global variables like  'local_infile';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Gasto.csv'
into table gasto 
fields terminated by ',' enclosed by '' escaped by ''
lines terminated by '\n' ignore 1 lines
;

select 
* from gasto;

create table compra (
	idCompra int,
    fecha date,
    idProducto int,
    cantidad int,
    precio decimal(10,2),
    idProveedor int
);

show variables like 'secure_file_priv';

load data local infile '\Users\PC ONE\Downloads\Gasto.csv'
into table compra
fields terminated by ',' enclosed by '' escaped by ''
lines terminated by '\n' ignore 1 lines
;

set global local_infile = 1;

load data infile ''
into table venta
fields terminated by ',' enclosed by '' escaped by ''
lines terminated by '\n' ignore 1 lines;

create table venta (
	idVenta int,
    fecha date, 
    fecha_entrega date,
    idCanal int,
    idCliente int,
    idSucursal int,
    idEmpleado int,
    idProducto int,
    precio varchar(50),
    cantidad varchar(50)
);

create table sucursal (
	id int,
    sucursal varchar(100),
    direccion varchar(200),
    localidad varchar(100),
    provincia varchar(100),
    latitud2 varchar(100),
    longitud2 varchar(100)
);

load data infile ''
into table sucursal
character set utf8mb4
fields terminated by ';' enclosed by '' escaped by '\"'
lines terminated by '\n' ignore 1 lines;

create table cliente (
	id int,
    provincia varchar(100),
    nombre_y_apellido varchar(200),
    domicilio varchar(100),
    telefono varchar(100),
    edad varchar(100),
    localidad varchar(100),
    x varchar(100),
    y varchar(100),
    fecha_alta date,
    usuario_alta varchar(100),
    fecha_ultima_modificacion date,
    usuario_ultima_modificacion varchar(100),
    marca_baja tinyint,
    col10 varchar(100)
);

load data infile ''
into table cliente
character set utf8mb4
fields terminated by ';' enclosed by '' escaped by '\"'
lines terminated by '\n' ignore 1 lines;

