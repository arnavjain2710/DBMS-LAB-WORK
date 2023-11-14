
-- Name: Arnav Jain
-- Roll No: 220002018


-- Q1 Using MySQL Workbench, create two schemas.
CREATE SCHEMA my_first_schema;
USE my_first_schema;
CREATE TABLE users (
  user_id INT NOT NULL,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (user_id)
);
CREATE SCHEMA my_second_schema;
USE my_second_schema;
CREATE TABLE products (
  product_id INT NOT NULL ,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (product_id)
);


-- Q2 Create Customer table with following attributes: Customer ID (primary key), name, age, city, mobile no. 
create database Customers;
use Customers;
CREATE TABLE Customer (
  customer_id INT NOT NULL ,
  name VARCHAR(255) NOT NULL,
  age INT,
  city VARCHAR(255),
  mobile_no bigint,
  PRIMARY KEY (customer_id)
);


-- Q3 Insert 10 records into Customer table.
insert into Customer(name , age , city , mobile_no , customer_id)
values
('Arnav',19,'Pune',99999999,2),
('Amit Sharma', 30, 'Delhi', 98111223344, 1),
('Priyanka Jain', 25, 'Mumbai', 99223344556 , 3),
('Rohan Khanna', 40, 'Chennai', 97334455667, 4),
('Sakshi Mehta', 35, 'Indore', 96445566778 , 5),
('Aditya Gupta', 20, 'Hyderabad', 95566778890 , 6),
('Shruti Agarwal', 25, 'Bengaluru', 94667788991,7),
('Rishabh Kapoor', 30, 'Hyderabad', 93778899002 , 8),
('Shraddha Desai', 35, 'Jaipur', 92889900113 , 9),
('Tanmay Singh', 40, 'Lucknow', 91990011224  ,10);


-- Q4 Alter Customer table by adding a new column order_id.
alter table Customer
add order_id int;


-- Q5 Delete a customer from Customer table where customer_id is equal to 1. 
delete from Customer 
where customer_id =1;


-- Q6 Display the name of the youngest customer(s) in Customer table.
select name 
from Customer
where age =(
 select min(age)
 from Customer
 );


-- Q7 Display all the customers from Customer table who live in Indore city.
select name
from Customer 
where city = "Indore";


-- Q8 Display all the customers from Customer table who are 25+ years old.
select name
from Customer
where age > 25;


-- Q9 Display all the customers from the Customer table who live either in Indore or Delhi or Chennai or Bengaluru or Hyderabad.
select name
from Customer
where city in("Indore" , "Delhi" , "Bengaluru" , "Hyderabad");


-- Q10 Delete/drop Customer table.
drop table Customer;

