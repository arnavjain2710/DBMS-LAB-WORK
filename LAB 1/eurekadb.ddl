drop database eurekadb  ;  
create database eurekadb; 
use eurekadb ;

create table employee(
employee_name varchar(255) NOT NULL,
street varchar(255) NOT NULL, 
city varchar(255) NOT NULL, 
join_date date NOT NULL
);

create table works(
employee_name varchar(255) NOT NULL,
 department_name varchar(255) NOT NULL,
 job_title varchar(255) NOT NULL,
 annual_salary float(25), 
 notes varchar(255) NOT NULL
);

create table department(
department_name varchar(255) NOT NULL ,
city varchar(255) NOT NULL
);

create table manages(
employee_name varchar(255) NOT NULL,
manager_name varchar(255) NOT NULL
);























