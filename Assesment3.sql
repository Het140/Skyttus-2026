CREATE DATABASE Company_DB;

CREATE TABLE employees (
 emp_id INT,
 emp_name VARCHAR(50),
 dept_id INT,
 salary INT
 ); 
 create table department(
 dept_id INT,
 dept_name VARCHAR(50)
 );
 INSERT INTO employees VALUES
 (1,'Het Patel',12,55000),
 (2,'Drish Bhandari',18,43000),
 (3,'Meet Patel',15,46000),
 (4,'Jay Patel',12,34000),
 (5,'Sujal Tandel',14,46000);

 INSERT INTO department values
 (12,'Python'),
 (18,'AI/ML'),
 (15,'FrontEnd Development'),
 (14,'Data');

 SELECT * FROM employees;
 SELECT * FROM department;

--Tasks Display employee name with department name 
select e.emp_name, d.dept_name
from employees e
JOIN department d
ON e.dept_id = d.dept_id;
--Display employees earning more than 50,000 
select emp_name, salary from employees where salary > 50000;
--Display department-wise total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN department d
ON e.dept_id = d.dept_id
group by d.dept_name;
--Display departments with more than 2 employees 
select d.dept_name, count(e.emp_id) as employee_count
from employees e
join department d
on e.dept_id = d.dept_id
group by d.dept_name
Having count(e.emp_id) > 2; 
--Display employees without a department	
select emp_name 
from employees
where dept_id is null;