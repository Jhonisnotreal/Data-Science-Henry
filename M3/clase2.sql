use adventureworks;

select 
* from
product limit 100;

select * from 
inventory 
limit 100;

select a.productid, a.name, b.* 
from product a
inner join productinventory b
on a.productid = b.productid
limit 100;

select count(*)
from product a 
left join 
productinventory b
on a.productid = b.productid
;


select distinct
a.productid, a.name
from product a
inner join productinventory b
on a.productid = b.productid
limit 100;