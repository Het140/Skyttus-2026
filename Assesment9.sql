create database employee;
use employee;

create table employee (
emp_id INT,
emp_name VARCHAR(50),
salary INT,
hire_date Date
);

INSERT INTO employee VALUES
(1, 'Het', 60000, '2025-01-12'),
(2, 'Jay', 50000, '2023-12-10'),
(3, 'Sujal', 60000, '2025-07-01'),
(4, 'Rahul', 40000, '2025-01-10'),
(5, 'Heli', 55000, '2025-01-01');

SELECT*FROM employee;

CREATE TABLE employees_backup (
emp_id INT,
emp_name VARCHAR(50),
salary INT
);

ALTER TABLE employees_backup
ALTER COLUMN emp_name VARCHAR(50);


INSERT INTO employees_backup VALUES
(1, 'Het', 60000),
(2, 'Jay', 50000),
(3, 'Sujal', 60000),
(4, 'Rahul', 40000),
(5, 'Heli', 55000);

 SELECT * FROM employees_backup;

 CREATE TABLE logs (
 id INT, 
 value INT
 );

 INSERT INTO logs VALUES
(1, 10),
(2, 10),
(3, 10),
(4, 20),
(5, 20),
(6, 30),
(7, 10),
(8, 10);
 
SELECT * FROM logs;


--Write query to find Nth highest salary 
SELECT salary
FROM ( SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employee) t
where rnk = 2;

--Remove duplicate records 
DELETE FROM employee
where emp_id NOT IN (SELECT MIN(emp_id) FROM employee GROUP BY emp_name, salary, hire_date );

--Find records common in two tables 
SELECT* FROM employee e
INNER JOIN employees_backup b
on e.emp_id = b.emp_id
AND e.salary = b.salary;

--Find employees hired in last 6 months 
SELECT* FROM employee
where hire_date >= DATEADD(MONTH, -6, GETDATE());

--Find continuous duplicate values
SELECT DISTINCT value
FROM(SELECT value, LAG(value) OVER (ORDER BY id) AS prev_value FROM logs) t
WHERE value = prev_value;