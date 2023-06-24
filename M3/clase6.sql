use henry_01;
show tables;

select * from cliente;

alter table cliente change ID IdCliente int not null;
alter table empleado change IdEmpleado IDEmpleado int null default null;
alter table empleado change IdProveedor IDProveedor int;
show tables;


