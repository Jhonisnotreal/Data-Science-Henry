use henry;

select count(idCarrera) as 'conteo carreras' from  carrera;

select count(idAlumno) as 'Cantidad de Alumnos' from alumno;

select count(idAlumno) as 'Cantidad de Alumnos', idCohorte as 'Numero de Cohorte' from alumno
group by idCohorte;

select concat(nombre, ' ', apellido) as 'Nombre completo', fechaIngreso as 'Fecha Ingreso' from alumno
order by fechaIngreso desc;

select concat(nombre, ' ', apellido) as 'Nombre completo', fechaIngreso as 'Fecha Ingreso' from alumno
order by fechaIngreso asc limit 1;

select concat(nombre, ' ', apellido) as 'Nombre completo', fechaIngreso as 'Fecha Ingreso' from alumno
order by fechaIngreso desc limit 1;

select year(fechaIngreso) as 'Anio Ingreso', count(idAlumno) as 'Cantidad Alumnos' from alumno
group by year(fechaIngreso) order by year(fechaIngreso);

select year(fechaIngreso) as 'Anio ingreso', weekofyear(fechaIngreso) as 'Semana Ingreso', count(idAlumno) as 
'Cantidad Alumnos' from alumno
group by year(fechaIngreso),
weekofyear(fechaIngreso) order by year(fechaIngreso), weekofyear(fechaIngreso);

select year(fechaIngreso) as 'Anio ingreso', weekofyear(fechaIngreso) as 'Semana Ingreso', count(idAlumno) as 
'Cantidad Alumnos' from alumno
group by year(fechaIngreso) having count(idAlumno) > 20;

select * from instructor;

select nombre, apellido, cumpleanios, timestampdiff(year, cumpleanios, curdate()) as 'Edad'
from instructor;

select nombre, apellido, cumpleanios, timestampdiff(year, cumpleanios, curdate()) as 'Edad',
date_add(cumpleanios, interval timestampdiff(year, cumpleanios, curdate()) year ) as 'Ultimo 
Cumpleanios' from instructor 
order by date_add(cumpleanios, interval timestampdiff(year, 
cumpleanios, curdate()) year ) asc;

-- calcular de cada alumno
select nombre, apellido, cumpleanios, timestampdiff(year, cumpleanios, curdate()) as 'Edad'
from alumno;

-- calcular la edad promedio de cada alumno
select nombre, apellido, cumpleanios, avg(timestampdiff(year, cumpleanios, curdate())) as 
'Edad Promedio' from instructor;

select nombre, apellido, cumpleanios, avg(timestampdiff(year, cumpleanios, curdate())) as 
'Edad Promedio', idCohorte as 'Numero de Cohorte' from alumno
group by idCohorte;

-- Alumnos que superen la edad promedio
select concat(nombre, ' ', apellido) as 'Nombre comleto', timestampdiff(year, cumpleanios, curdate()) as 
'Edad' from alumno
where timestampdiff(year, cumpleanios, curdate()) > (select avg(timestampdiff(year, cumpleanios, curdate())) from alumno)
order by timestampdiff(year, cumpleanios, curdate());

