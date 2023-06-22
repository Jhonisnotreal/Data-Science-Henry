use mydb_2023;
select * from transactions2;

insert into transactions2 (amount, customer_id)
values (1.00, NULL);

select * from customers;

insert into customers (first_name, last_name)
values ("Poppy", "Puff");


select transaction_id, amount, first_name, last_name 
from transactions2 inner join customers 
on transactions2.customer_id = customers.customer_id;

select *
from transactions2 left join customers
on transactions2.customer_id = customers.customer_id;

select *
from transactions2 right join customers
on transactions2.customer_id = customers.customer_id;