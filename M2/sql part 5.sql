create table customers (
	customer_id int primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50)
);

select * from customers;

insert into customers (first_name, last_name)
values ("Fred", "Fish"), ("Larry", "Lobster"), ("Chino", "Pacas");

drop table transactions2;

create table transactions2 (
	transaction_id int primary key auto_increment,
    amount decimal(5,2),
    customer_id int,
    foreign key(customer_id) references customers(customer_id)
);

select * from transactions2;

alter table transactions2
drop foreign key transactions2_ibfk_1;

alter table transactions2
add constraint fk_customer_id
foreign key(customer_id) references customers(customer_id);

delete from transactions2;

alter table transactions2
auto_increment = 1000;

select * from transactions2;

insert into transactions2 (amount, customer_id)
values (4.99, 3), (2.89, 2), (3.37, 3), (4.88,1);

delete from transations2
where customer_id = 3;