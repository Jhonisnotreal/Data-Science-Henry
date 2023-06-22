select first_name, last_name 
from employees;

select first_name, last_name 
from employees
where employee_id = 1;

select first_name, last_name 
from employees
where first_name = 'Spongebob';

select *
from employees
where hourly_pay >= 15;

select * 
from employees 
where hire_date <= "2023-01-03";

select *
from employees
where employee_id != 1;

select *
from employees
where hire_date is null;

select *
from employees
where hire_date is not null;
-- -----------------------------
update employees 
set hourly_pay = 10.50,
	hire_date = "2023-01-07"
where employee_id = 6;

select * from employees;
	
update employees 
set hire_date = Null
where employee_id = 6;

-- NO HAGAS ESTO PORQUE AFECTAS A TODA LA COLUMNA:
update employees 
set hourly_pay = 10.50;
-- SERIOUSLY DON'T THAT, AND THIS:
delete from employees;
-- STOP IT
delete from employees
where employee_id = 6;

select * from employees;

