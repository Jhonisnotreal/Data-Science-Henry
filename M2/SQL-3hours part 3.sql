select * from employees;
set autocommit = on; #guardar cada cambio manualmente
rollback;
commit;

create table test(
		my_date date, 
        my_time time,
        my_datetime datetime
);

select * from test;

insert into test 
values(current_date(), current_time(), now());
-- values(current_date() + 1, null, null);

create table products(
	id int,
    product_name varchar(25) unique,
    price decimal(4, 2)
);

alter table products
add constraint 
unique(product_name);

select * from products;

insert into products
values (100, "hamburguer", 3.99), (101, "Fries", 1.89), (102, "soda", 1.00), (103, "ice cream", 1.49);

alter table products
modify price decimal(4,2) not null;

insert into products
values (104, "cookie", 0);

select * from employees;

alter table employees
add constraint chk_hourly_pay check(hourly_pay >= 10.00);

insert into employees
values (6, "Sheldon", "Plankton", 10.00, "2023-01-07");

alter table employees
drop check chk_hourly_pay;

select * from products;

insert into products
values (104, 'straw', 0.00), (105, 'napkin', 0.00), (106, 'fork', 0.00), (107, 'spoon', 0.00);

delete from products 
where id >= 104;

alter table products
alter price set default 0;

insert into products (id, product_name)
values (104, "straw"), (105, "napkin"), (106, "fork"), (107, "spoon");

create table transactions(
	id int,
    amount decimal(5,2),
    transaction_date datetime default now()
);

select * from transactions;

insert into transactions (id, amount)
values (1, 4.99);

insert into transactions (id, amount)
values (1, 3.89);