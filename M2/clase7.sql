select * from alumno
order by idAlumno desc;
-- order by por defecto es asc

select nombre, aprellido, fechaIngreso
from alumno
where carrera = "Data Science"
limit 5,10;

select count(*)
from alumno
where carrera = "Data Science";
-- count() para cantidad de filas

select count(fechaFinalizacion) from alumno;

select carrera.nombre as "Nombre Carrerra", count(idAlumno) as "Cantidad Alumnos" from alumno
join cohorte 
on cohorte.idCohorte = alumno.idCohorte
join carrera
on cohorte.idCarrera = carrera.idCarrera
where carrera.nombre = "Data Scientist";
-- group by carrera.nombre;

-- sum(), avg(), max(), min()
select sum(idAlumno) from alumno;

use subte;
select year(fecha), month(fecha), sum(cantidad) from subte
group by year(fecha), month(fecha);

select year(fecha), month(fecha), max(sum(cantidad))
from subte
group by year(fecha), month(fecha)
order by sum(cantidad)
limit 1;

select idCohorte, count(idAlumno)
from alumno
group by idCohorte
having idCohorte >= 1240;