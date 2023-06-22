-- FUNCTIONS

select count(amount) as "today's transactions"
from transactions2;

select max(amount) as maximum
from transactions2;

select min(amount) 
from transactions2;

select avg(amount) as promedio	
from transactions2;

select avg(amount) as promedio	
from transactions2;

select sum(amount)
from transactions2;

select concat(first_name, " ", last_name) as full_name
from employees;

alter table employees
add column job varchar(25) after hourly_pay;

select * from employees;

update employees
set job = "janitor"
where employee_id = 6;

select * from employees
where hire_date < "2023-01-5" and job = "cook";

select * from employees
where job = "cook" or job = "cashier";

select * from employees
where not job = "manager" and not job = "asst. manager";

select * from employees
where hire_date between "2023-01-04" and "2023-01-07";

select * from employees
where job in ("cook", "cashier", "janitor");