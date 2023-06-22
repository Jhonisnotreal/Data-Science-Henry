use transporte;
select * from tipo_transporte;

select * from tren;

use locales;
select * from oferta_gastronomica where categoria = 'PUB';

select barrio, count(id) from oferta_gastronomica
where categoria = 'PUB'
group by barrio 
order by count(id) desc
limit 1;


select categoria, count(id) from oferta_gastronomica
group by categoria
order by count(id) desc;

select comuna, count(id) from oferta_gastronomica
where categoria = 'RESTAURANTE'
group by comuna
order by count(id);