use adventureworks;

select * from salesorderdetail;
select * from salesorderheader;

delimiter $$
create procedure totalOrdenes(in fecha date)
begin
	select 
    count(*) as numeroOrdenes
    from salesorderheader
    where date(orderdate) = fecha;
end $$

delimiter ;
call totalOrdenes('2002-07-01');
-- orderdate es de salesorderheader timestampp

# crear una funcion que calcule el margen bruto

set global log_bin_trust_function_creators = 1;

delimiter $$
create function margenBruto(precio double, margen double) returns double
begin
	declare resultado double;
    set resultado = margen * precio;
    return resultado;
end $$

delimiter ; 


# Obtener un listado de productos en orden alfabetico que muestre cual deberia ser el valor
select
productId, name, ListPrice, 
margenBruto(StandardCost, 1.2) as ListPriceMargen, ListPrice - margenBruto(StandardCost, 1.2) as Diferencia
from producto
order by name asc;

#crear un procedimiento que reciba como parametro



delimiter $$
create procedure totalTransporte (in fechaDesde date, in fechaHasta date)
begin
	select customerId, sum(freight) as TotalTransporte
    from salesorderheader
    where date(orderdate) between fechaDesde and fechaHasta
    group by customerId
    order by 
    sum(freight) desc
    limit 10
    ;
end $$

delimiter ;

call totalTransporte('2001-01-01', '2003-01-01');

#crear un procedimiento que permita realizar la insercion de datos en la tabla shipmethod
select * 
from shipmethod;

delimiter $$
create procedure insertShip(in nombre varchar(100), in shipbase double, in rate double)
begin
	insert into shipmethod(Name, ShipBase, ShipRate, rowguid, ModifiedDate)
	values (nombre, shipbase, rate, '', now() );
end $$    

delimiter ;

call insertShip('prueba2', 14.5, 0.75);

select * from shipmethod;