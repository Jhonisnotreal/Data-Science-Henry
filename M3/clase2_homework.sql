use adventureworks;

--  Obtener un listado contactos que hayan ordenado productos de la subcategoría "Mountain Bikes", entre los años 2000 y 
-- 2003, cuyo método de envío sea "CARGO TRANSPORT 5".<br>

show tables;

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

select * from productcategory;
select * from shipmethod;
select * from productsubcategory;
select * from salesorderheader;
select * from product;
select * from contact;

select p.*, s.*
from productcategory p
join productsubcategory s 
on s.productcategoryid = p.productcategoryid
where s.name like '%mountain bikes%'
;

select s.*, m.shipmethodid
from salesorderheader s
join shipmethod m
on m.shipmethodid = s.shipmethodid
where m.shipmethodid = 5
;

-- Obtener un listado contactos que hayan ordenado productos de la subcategoría "Mountain Bikes", 
-- entre los años 2000 y 2003 con la cantidad de 
-- productos adquiridos y ordenado por este valor, de forma descendente.

select * from salesorderheader;
select * from product;

select * from productsubcategory;
select a.*, b.*
from product a 
inner join productsubcategory b
on a.productid = b.productid;

-- Obtener un listado de cual fue el volumen de compra (cantidad) por año y método de envío
select * from salesorderdetail;
select * from salesorderheader;
show tables;
select * from salesterritory;
select * from salesreason;
select * from salesorderheadersalesreason;
select * from purchaseorderdetail;
select * from purchaseorderheader;
select * from vendorcontact;
select * from vendoraddress;
select * from store;
select * from storecontact;
select * from productinventory;
select * from productdocument;
select * from productmodel;
select * from individual;




-- Obtener un listado por categoría de productos, con el valor total de ventas y productos vendidos.
select * from productcategory;


-- Obtener un listado por país (según la dirección de envío), con el valor total de ventas y 
-- productos vendidos, sólo para aquellos países donde se enviaron más de 15 mil productos

select 
r.name, sum(d.orderqty) as 'cantidad productos', sum(h.totaldue) as 'Total Venta'
from salesorderheader h
join salesorderdetail d
on h.salesorderid = d.salesorderid 
join address a
on h.shiptoaddressid = a.addressid
join stateprovince sp
on sp.stateprovinceid = a.stateprovinceid
join countryregion r
on sp.countryregioncode = r.countryregioncode
group by r.name
having sum(d.orderqty) > 15000
;

select * from salesorderdetail;
select * from stateprovince;
select * from address;
select * from countryregion;
select * from address;
select * from salesorderheader;

-- clientes que no han comprado nunca
select 
c.customerid
from customer c
left join salesorderheader h
on c.customerid = h.customerid
where h.salesorderid is null
;