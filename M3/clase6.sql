-- GUARDA LO BIEN!!!!!

use henry_01;
show tables;

select * from cliente;

alter table cliente change ID IdCliente int not null;
alter table empleado change IdEmpleado IDEmpleado int null default null;
alter table empleado change IdProveedor IDProveedor int;
show tables;

select distinct
localidad, provincia from cliente;

select distinct 
localidad, provincia from sucursal;

select distinct 
ciudad, provincia from ciudad;

insert into provincia(nombreProvincia)
select distinct
case
	when provincia like '%Aires%' then 'Buenos Aires'
    when provincia like '%Bs%' then 'Buenos Aires'
    when provincia like '%caba%' then 'Buenos Aires'
    when provincia like '%Tucuman%' then 'Tucumán'
else provincia 
end provincia_limpia
from (
	SELECT DISTINCT
	localidad,
	uc_words(localidad) as localidad_homologada,
	provincia
	FROM
	cliente
	UNION 
	SELECT DISTINCT
	localidad,
	uc_words(localidad) as localidad_homologada,
	provincia
	FROM
	sucursal
	UNION
	select
	ciudad, 
	uc_words(ciudad) as localidad_homologada,
	provincia
	from
	proveedor
) A;

create table provincia (
	idProvincia int primary key auto_increment,
    nombreProvincia varchar(100)
);

select * from provincia;

-- Localidad 
select distinct
localidad_homolagada, 
case
	when localidad_homolagada like '%capital%' then 'CABA'
    when localidad_homolagada like '%cap.%' then 'CABA'
    when localidad_homolagada like '%fed.%' then 'CABA'
    when localidad_homolagada like '%Capfed%' then 'CABA'
    when localidad_homolagada like '%Cdad De Buenos Aires%' then 'CABA'
else localidad_homolagada
end localidad_limpia
from (
	SELECT DISTINCT
	localidad,
	uc_words(localidad) as localidad_homologada,
	provincia
	FROM
	cliente
	UNION 
	SELECT DISTINCT
	localidad,
	uc_words(localidad) as localidad_homologada,
	provincia
	FROM
	sucursal
	UNION
	select
	ciudad, 
	uc_words(ciudad) as localidad_homologada,
	provincia
	from
	proveedor
) A
order by localidad_homolagada;

create table localidad (
	idLocalidad int primary key auto_increment,
    nombre varchar (100),
    idProvincia int
)

SELECT DISTINCT
localidad_limpia,
idprovincia
FROM
(
 SELECT DISTINCT
 CASE 
  WHEN localidad_homologada LIKE '%capital%' THEN 'CABA'
  WHEN localidad_homologada LIKE '%cap.%' THEN  'CABA'
  WHEN localidad_homologada LIKE '%fed.%' THEN 'CABA'
  WHEN localidad_homologada LIKE 'Capfed' THEN 'CABA'
  WHEN localidad_homologada LIKE 'Cdad De Buenos Aires' THEN 'CABA'
 ELSE localidad_homologada 
 END localidad_limpia,
 CASE
  WHEN provincia LIKE '%Aires%' THEN 'Buenos Aires'
  WHEN provincia LIKE '%Bs%' THEN 'Buenos Aires'
  WHEN provincia LIKE '%caba%' THEN 'Buenos Aires'
  WHEN provincia LIKE 'Tucuman' THEN 'Tucumán'
 ELSE provincia
 END provincia_limpia
 FROM
 (
  SELECT DISTINCT
  localidad,
  UC_Words(localidad) as localidad_homologada,
  provincia
  FROM
  cliente
  UNION 
  SELECT DISTINCT
  localidad,
  UC_Words(localidad) as localidad_homologada,
  provincia
  FROM
  sucursal
  UNION
  select
  ciudad, 
  UC_Words(ciudad) as localidad_homologada,
  provincia
  from
  proveedor
 ) A
) C
inner join
provincia B
ON C.provincia_limpia  = B.nombreProvincia;

-- La parte de arriba no la entiendooo
select * from proveedor;

alter table proveedor add column idProvincia int;
alter table proveedor add column idLocalidad int;

alter table sucursal add column idProvincia int;
alter table sucursal add column idLocalidad int;

select * from sucursal;


-- OUTLIERS
select * from venta;

select
case
	when precio > limiteSuperior or precio < limiteInferior then 1
    else 0
end as flag_outlier
from
(
	select 
    precio, 
    avg(precio) over() + 3 * STDdEV(precio) over() as limiteSuperior,
	avg(precio) over() - 3 * stddev(precio) over() as limiteInferior
	from venta
) A
where 
case
	when precio > limiteSuperior or precio < limiteInferior then 1
    else 0
end = 1
;