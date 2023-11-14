create database customer1;
use customer1;

-- Question 2 
create table customer12(
customer_id int,
name varchar(255),
age int,
city varchar(255),
mobileno bigint,
primary key(customer_id)
);

insert into customer12(customerid , name , city , mobileno)
values
(1, 'arnav' , 19 , 'indore' ,8847796758);

-- Question 9
select name
from customer12
where city in ('indore' , 'delhi' , 'chennai' , 'bengaluru' , 'hyderabad'); 