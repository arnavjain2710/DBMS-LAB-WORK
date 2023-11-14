use  eurekadb ;

-- Question 4 
-- a. Alter the schema of table works to first drop the column notes and then add the column again with type VARCHAR(150).

	ALTER TABLE works DROP COLUMN notes;
    ALTER TABLE works ADD COLUMN notes VARCHAR(150);

-- b. Update the annual salary of all employees who manage at least one employee by 10%.

UPDATE works
SET annual_salary = annual_salary * 1.1
WHERE employee_name IN (SELECT DISTINCT manager_name FROM manages);

-- c. Delete records of all employees who joined before 31-12-2008.

DELETE FROM employee
WHERE join_date < '2008-12-31';

-- Question 5
-- a. Names of employees who work in the ‘Human Resource’ department.

SELECT employee_name
FROM works
WHERE department_name = 'HR';

-- b. Name, salary and address (street, city) of EUREKA’s CFO.

SELECT M.employee_name, M.street, M.city
FROM (
SELECT M.employee_name, annual_salary, M.street, M.city
FROM employee as M
JOIN works
ON M.employee_name = works.employee_name
WHERE job_title = 'CFO') as M;

-- c. Names of employees who earn more than the average salary.

SELECT employee_name
FROM works
WHERE annual_salary > (
  SELECT AVG(annual_salary)
  FROM works
);

-- d. Names of employees who live in cities other than their department’s headquarter city.

SELECT e.employee_name, e.city, w.department_name
    FROM employee e
    JOIN works w on e.employee_name = w.employee_name
    JOIN department d ON w.department_name = d.department_name
    WHERE e.city != d.city;

-- e. Names of employees who live in the same cities and on the same streets as their managers.

SELECT a.employee_name
FROM employee AS a
JOIN manages
ON a.employee_name = manages.employee_name
JOIN employee AS m
ON manages.manager_name = m.employee_name
WHERE a.street = m.street
AND a.city = m.city;

-- f. Names of employees who earn more than the average salary of their department.

SELECT employee_name
FROM works
WHERE annual_salary > (
  SELECT AVG(annual_salary)
  FROM works
  WHERE department_name = works.department_name
);

-- g. Department with largest payroll (largest sum of all employee salaries).

select department_name
from (
    select department_name, SUM(annual_salary) as total_payroll
    from works
    group by department_name
    order by total_payroll desc
    limit 1
) as highest_dep;

-- h. Department with largest payroll per head.

select department_name
from (
    select department_name, SUM(annual_salary) / COUNT(employee_name) as payroll_per_head
    from works
    group by department_name
    order by payroll_per_head desc
    limit 1
) as high_dep_per_head;

 
 
 


