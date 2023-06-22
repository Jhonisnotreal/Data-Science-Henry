#create database myDB_2023;
use myDB_2023; #right click -- set as default schema 
#drop database myDB_2023;

#alter database myDB_2023 read only = 0; #we can't do modifications

create table employees (
	employee_id int, 
    first_name varchar(50),
    last_name varchar(50),
    hourly_pay decimal(5, 2),
    hire_date date
);

select * from employees;

rename table employees to workers;
rename table workers to employees;
#drop table employees;
alter table employees 
add phone_number varchar(15);

alter table employees 
rename column phone_number to email;

alter table employees
modify column email varchar(100);

alter table employees
modify email varchar(100) 
#after last_name; 
first;

select * from employees;

alter table employees
drop column email;

insert into employees 
values (1, "Eugene", "Krabs", 25.50, "2023-01-02");

insert into employees 
values 	(2, "Squidward", "Tentacles", 15.00, "2023-01-03"),
		(3, "Spongebob", "Squarepants", 12.50, "2023-01-04"),
        (4, "Patrick", "Star", 12.50, "2023-01-05"),
        (5, "Sandy", "Cheeks", 17.25, "2023-01-06");

insert into employees(employee_id, first_name, last_name) 
values 	(6, "Sheldon", "Plankton");

select * from employees;