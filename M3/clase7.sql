use henry_01;


-- Agregar PK 
alter table canalVenta add primary key (idCanalVenta);
alter table venta add primary key (idVenta);
alter table cliente add primary key (idCliente);



select * from canalVenta;
describe canalVenta;

select * from venta;
describe venta;

select * from cliente;
describe cliente;

-- Agregar indices 
alter table venta add index (fecha);
alter table venta add index (fecha_entrega);
alter table venta add index (idCliente);
alter table venta add index (idCanal);
alter table venta add index (idProducto);
alter table cliente add index (fecha_alta);
alter table cliente add index (fecha_ultima_modificacion);
alter table cliente add index (nombre_y_apellido);

show index from cliente;
show index from venta;

drop index fecha_2 on venta;
select * from cliente;

create table fact_venta(
	idVenta int,
    Fecha date, 
    Fecha_Entrega date,
	IdCanal int,
    IdCliente int,
    IdEmpleado int,
    IdProducto int,
    Precio decimal(10,2),
    Cantidad decimal(10,2)
);    
    
-- insert into fact_venta
select * from fact_venta;