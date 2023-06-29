show databases;
use henry_01;

-- Calidad del dato
-- Normalizacion

show tables;

select 
* 
from 
cliente;

-- Cambiar el nombre de ids
alter table cliente change idcliente idCliente int not null;

-- Verificando que los id sean unicos
select
IdCliente, 
count(*)
from 
cliente
group by 1
having count(*) > 1;
-- o sea no hay un cliente con mas de id que debe ser unico

show tables;
select 
*
from 
empleados;

select
id_empleado, 
count(*)
from 
empleados
group by 1
having count(*) > 1;

alter table empleados change id_empleado idEmpleado int null default null;

select
*
from empleados where idEmpleado is null;

alter table proveedor change idproveedor idProveedor int;
alter table sucursal change id idSucursal int;
alter table producto change concepto Producto varchar(100);

select idProducto, count(*) from producto group by 1
having count(*) > 1; -- ya vi que no hay duplicados 

select distinct idProducto, Producto from producto;

-- CORREGIR TIPOS DE DATOS 
select * from cliente;
-- 1. Crear una nueva columna para latitud y longitud (x, y en nuestra tabla cliente)
-- alter table cliente drop column latitud;
-- alter table cliente drop column longitud;
alter table cliente add latitud double default 0 after x;
alter table cliente add longitud double default 0 after y;
-- alter table cliente drop x;
-- alter table cliente drop y;

update cliente
set x = '0'
where x = '';

update cliente
set y = '0'
where y = '';

-- cambiando las ',' por '.' en cliente
update cliente 
set latitud = replace(x, ',', '.');

update cliente 
set longitud = replace(y, ',', '.');
select 
replace(x,',','.'),
x
from cliente;

-- solucionando tabla empleados
select * from empleados;

alter table empleados change salario salario decimal(10,2);
alter table empleados rename column salario to Salario;

-- Alterando tabla producto
select * from producto;
describe producto;
-- todo esta bien no hay nada que reemplazar 
-- Alterando tabla sucursal
select * from sucursal;
alter table sucursal add latitud double;
alter table sucursal add longitud double;

update sucursal 
set latitud = replace(latitud2, ',', '.');

update sucursal 
set longitud = replace(longitud2, ',', '.');

alter table sucursal drop latitud2;
alter table sucursal drop longitud2;

-- Alterando la tabla venta
select * from venta;

update venta
set precio = '0'
where trim(precio) = '';
describe venta;

alter table venta modify precio decimal(10,2);

update venta
set cantidad = '0'
where trim(cantidad) = '\r';

alter table venta modify cantidad int;

-- alterando cliente
select * from cliente;
alter table cliente drop col10;


-- Valores Faltantes
select * from cliente;
describe cliente;

update cliente 
set provincia = 'Sin Dato'
where trim(provincia) = '';

update cliente
set localidad = 'Sin Dato' where trim(localidad) = '';

update cliente
set nombre_y_apellido = 'Sin Dato' where trim(nombre_y_apellido) = '';

update cliente
set domicilio = 'Sin Dato' where trim(domicilio) = '';

update cliente
set usuario_alta = 'No identificado' where trim(usuario_alta) = '';

update cliente
set usuario_ultima_modificacion = 'Sin Dato' where trim(usuario_ultima_modificacion) = '';

-- Alterando tabla empleados

-- min 1 43 58