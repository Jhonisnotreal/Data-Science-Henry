-- Triggers y Carga incremental
use henry_01;
show tables;

select * from cliente;

describe cliente;

delimiter //
create trigger validarEdad before insert on cliente for each row
begin
	if new.edad < 0 then
	set new.edad = abs(new.edad);
    end if;    
end //

delimiter ;



select * from cliente;
select max(id) from cliente;

insert into cliente (ID, nombre_y_apellido, edad)
values(3408, 'Juan Janett', -10);

select * from cliente where id = 3408;


-- drop trigger validarEdad;

delimiter //
create trigger validarEdad before insert on cliente for each row
begin
	if new.edad < 0 then
	set new.edad = abs(new.edad);
    set new.usuario_alta = user();
    set new.fecha_alta = cast(now() as date);
    set new.nombre_y_apellido = upper(new.nombre_y_apellido);
    end if;    
end //

delimiter ;



insert into cliente (id, nombre_y_apellido, edad)
values (3409, 'Juan Janett Hernandez', -25);

select * from cliente where id = 3409;


delimiter //
create trigger validarEdad_existente before update on cliente for each row
begin
	set new.fecha_ultima_modificacion = cast(now() as date);
    set new.usuario_ultima_modificacion = user();
end //

delimiter ;

update cliente
set nombre_y_apellido = "Juan J Janett"
where id = 3409;

select * from cliente where id = 3409;

create table auditoria_cliente
(
	fecha datetime,
    usuario varchar(100),
    nombre_anterior varchar(100),
    nombre_nuevo varchar(100)
);


delimiter //
create trigger registroAuditoria after update on cliente for each row
insert into auditoria_cliente values(now(), user(), old.nombre_y_apellido, new.nombre_y_apellido);


delimiter ;

update cliente
set nombre_y_apellido = "CJNG"
where id = 3409;


select * from auditoria_cliente;