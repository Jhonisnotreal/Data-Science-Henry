select * from employees
where first_name like "s%";

select * from employees
where last_name like "%r";

select * from employees
where first_name like "sp%";

select * from employees
where job like "_ook%"; -- random character

select * from employees
where hire_date like "____-__-03";

select * from employees
where job like "_a%";

select * from employees
order by last_name desc;

select * from transactions2
order by amount, customer_id;

select * from employees
order by last_name desc limit 4; 

select * from employees
limit 1, 1;

select * from employees
limit 3, 1; -- limit 30, 10;

create table income (
	income_name varchar(30),
    amount decimal
);

