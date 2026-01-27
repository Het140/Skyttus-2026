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

UPDATE employees
SET salary = 43000
WHERE emp_id = 2;


--Tasks Find employees earning more than average salary 
select emp_name, salary
from employees
where salary > (
select AVG(salary)
from employees
);
--Find department with highest total salary 
select d.dept_name, SUM(e.salary) as total_salary
From employees e
join department d
on e.dept_id = d.dept_id
group by d.dept_name
order by total_salary DESC;

--Display employee with second highest salary 
select * from employees
where salary = ( select max(salary)
from employees where salary < (
select max(salary)
From employees
)
);
--Display employees working in same department as "Amit"
select emp_name, dept_id
from employees
where dept_id = (
SELECT dept_id
from employees
where emp_name like 'Amit%'
);