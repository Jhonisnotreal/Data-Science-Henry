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

select * from gasto;

show tables;

create table compra (
	idCompra int,
    fecha date,
    idProducto int,
    cantidad int,
    precio decimal(10,2),
    idProveedor int
);

show variables like 'secure_file_priv';

load data local infile 'C:/Users/PC ONE/OneDrive/Escritorio/DS Henry/M3/Homework/Compra.csv'
into table compra
fields terminated by ',' enclosed by '' escaped by ''
lines terminated by '\n' ignore 1 lines
;


set global local_infile = 1;

load data local infile 'C:/Users/PC ONE/OneDrive/Escritorio/DS Henry/M3/Homework/Venta.csv'
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

load data local infile 'C:/Users/PC ONE/OneDrive/Escritorio/DS Henry/M3/Homework/Sucursales.csv'
into table sucursal
character set utf8mb4
fields terminated by ';' enclosed by '' escaped by '\"'
lines terminated by '\n' ignore 1 lines;


create table cliente (
	id int,
    provincia varchar(100),
    nombre_y_apellido varchar(200),
    domicilio varchar(200),
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

load data local infile 'C:/Users/PC ONE/OneDrive/Escritorio/DS Henry/M3/Homework/Clientes.csv'
into table cliente
character set utf8mb4
fields terminated by ';' enclosed by '' escaped by '\"'
lines terminated by '\n' ignore 1 lines;

select count(*) from cliente;

create table proveedor(
	IDProveedor int,
    Nombre varchar(100),
    Domicilio varchar(100),
    ciudad varchar(100),
    Provincia varchar(100),
    Pais varchar(100),
    Departamento varchar(100)
);
	
describe proveedor;

create table empleados(
	ID_empleado int,
    Apellido varchar(100),
    Nombre varchar(100),
    Sucursal varchar(100),
    Sector varchar(100),
    Cargo varchar(100),
    Salario varchar(100)
);

select * from empleados;
describe empleados;

create table tipoGasto(
	idTipoGasto int,
    Descripcion varchar(100),
    Monto_Aproximado double
);
drop table tipoGasto;

load data local infile 'C:/Users/PC ONE/OneDrive/Escritorio/DS Henry/M3/Homework_Resuelto/TiposDeGasto.csv'
into table tipoGasto
fields terminated by ';' enclosed by '' escaped by '\"'
lines terminated by '\n' ignore 1 lines;

select * from tipoGasto;

create table producto(
	idProducto int,
    Concepto varchar(100),
    Tipo varchar(100),
    Precio decimal(20,2)
);

create table canalVenta(
	idCanalVenta int,
    Descripcion varchar(100)
);