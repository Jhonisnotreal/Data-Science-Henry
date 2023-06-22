create database Henry; -- Instruccion DDL - Data Definition Language
-- drop database Henry;
use Henry;
create table alumno (
	cedulaIdentidad int not null auto_increment,
    nombre varchar(50),
    apellido varchar(50),
    fechaInicio date,
    primary key (cedulaIdentidad)
);

alter table alumno
add direccion varchar(40);

select * from alumno;

-- drop table alumno;

create table carrera(
	id int primary key auto_increment,
    nombre varchar(20),
    id_alumno int,
    foreign key (id_alumno) references alumno(cedulaIdentidad)
);

select * from carrera;
-- drop table carrera;

-- Tarea :


-- 02-06-2023
insert into carrera (nombre)
values ('Full Stack Developer'), ('Data Science');

create table instructor(
	id int primary key auto_increment,
    nombre varchar(20),
    apellido varchar(20),
	cumpleanios date,
    fechaIngreso date
);

insert into instructor (nombre, apellido, cumpleanios, fechaIngreso)
values ('Lucia', 'Fernanda', '1999-5-25', '2019-8-23'),
('Marco', 'Lopez', '2000-6-13', '2018-5-29');

create table cohorte(
	id int primary key auto_increment,
    codigo varchar(10),
    idCarrera int,
    idInstructor int,
    Inicio date,
    Termino date
);

select * from instructor
where nombre = 'Lucia' or apellido = 'Lopez';

-- delete from instructor
-- where nombre = 'Marcos' or apellido = 'Lopez';

select * from alumno
where cedulaIdentidad = null;

select * from instructor;

update instructor 
set cumpleanios = '2001-7-24' 
where nombre = 'Lucia' and apellido = 'Fernanda';

select nombre, apellido, fechaIngreso from instructor
where id = 1;

-- select distinct nombre from instructor; -- esto trae los valores unicos
select * from alumno where idCohorte = 1235
and fechaIngreso like '2019%';

select * from alumno where idCohorte = 1235
and year(fechaIngreso) = '2019';

select alumno.nombre, alumno.apellido, alumno.fechaNacimiento, carrera.nombre
from alumno
inner join cohorte
on cohorte.idCohorte = alumno.idCohorte
inner join carrera
on carrera.idCarrera = cohorte.idCohorte
where carrera.nombre like 'Full Stack Developer';
-- where carrera.nombre not like 'Data Science';
-- where carrera.nombre = 'Full Stack Developer';
-- where carrera.nombre != 'Data Science';
-- where carrera.idCarrera = 1;

