use adventureworks;


select 
A.productid, A.totalunidades, B.unidadesVendidas, C.name
from
(
	select 
	productid, sum(quantity) as totalunidades
	from 
	productinventory
	group by productid
) A
inner join
(
	select 
	productid, sum(orderqty) as unidadesVendidas
	from
	salesorderdetail
	group by
	productid
) B
on A.productid = B.productid
inner join
product C
on A.productid = C.productid;

select
*
from 
product;

select 
distinct productid
from
productinventory;

select 
* 
from
product
where
productid in
(select distinct
productid
from 
productinventory);

select 
* 
from 
product
where
productid not in 
(select distinct
productid
from 
productinventory);

select
*
from
(
	select
	productid, sum(linetotal) as totalVenta, sum(orderqty) as totalUnidades
	from
	salesorderdetail
	group by 
	productid
) A
inner join
(
	select
	productid, sum(quantity) as totalInventario
	from
	productinventory
	group by 
	productid
) B;


select 
* 
from 
salesorderdetail;

select 
*
from product;

-- Creando vista

create view contactos as
select distinct
o.ContactID,
o.firstname, 
o.lastname
from salesorderheader h
join salesorderdetail d 
on h.salesorderid = d.salesorderid
join product p 
on d.productid = p.productid
join productsubcategory s
on s.productsubcategoryid = p.productsubcategoryid 
join shipmethod m
on h.shipmethodid = m.shipmethodid
join contact o
on o.contactid = h.contactid
where s.name = 'Mountain Bikes' 
and year(h.orderdate) between 2000 and 2003 
and m.name = 'CARGO TRANSPORT 5'
limit 10
;

select 
*
from contactos
;

-- Funciones Ventana

select 
*,
row_number() over (order by productid), -- enumera filas
row_number() over (order by productid desc)
from
productinventory
order by productid
;

-- LEAD y LAG
create view vendedores as
select
salespersonid, territoryid, round(sum(totaldue), 2) as venta_acumulada
from
salesorderheader
group by
salespersonid, TerritoryID
having salespersonid is not null
order by
territoryid, sum(totaldue) desc
;

select
*,
lag(venta_acumulada, 1, null) over (partition by territoryid order by venta_acumulada desc) - venta_acumulada as restante
from vendedores
;


