create table transactions2(
	transaction_id int primary key,
    amount decimal(5, 2)
);

select * from transactions2;

alter table transactions2
add constraint 
primary key(transaction_id);

insert into transactions2
values (1000, 4.99);

insert into transactions2
values (1001, 3.39);

select amount from transactions2 
where transaction_id = 1000;

drop table transactions2;

create table transactions2 (
	transaction_id int primary key auto_increment,
    amount decimal(5,2)
);

select * from transactions2;

insert into transactions2 (amount)
values (2.89), (3.38), (5.32);

alter table transactions2 
auto_increment = 1000;

delete from transactions2;

