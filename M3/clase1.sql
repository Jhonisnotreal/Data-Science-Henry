use henry;


-- Variables: 
set @carrera = 'Data Science', @carrera2 = 'Fullstack';
select @carrera, @carrera2;

use checkpoint_m2;
select * from venta;

set @anio = 2018;

select * 
from venta where year(fecha) = @anio;

select @fecha := fecha from venta
where year(fecha) = 2019;

select @fecha;

select fecha from venta
where fecha = @fecha;

select @promedio := avg(precio) from venta
where precio < 700;

select @promedio;

show databases;
show tables;
show variables;

--  	FUNCIONES

-- AVG, concatenate, year, sum, timestampdiff, sum;
-- el sistema, la sesion, entorno:

set global log_bin_trust_function_creators = 1; -- Para crear funciones

-- Creando funcion:
delimiter $$
create function antMeses(fechaIngreso date) returns int
begin 
	declare meses int;
	set meses = timestampdiff(month, fechaIngreso, curdate());
    return meses;
end$$
delimiter ;

select antMeses('2019-05-05');
set @ant_meses = antMeses('2019-05-05');
select @ant_meses;

-- Crear un procedimiento

delimiter $$
create procedure getTotalAlumnos()
begin 
	declare cantidad int default 0;
    select count(*) into cantidad
    from venta;
	
    select cantidad;
end;
delimiter ;

call getTotalAlumnos();

