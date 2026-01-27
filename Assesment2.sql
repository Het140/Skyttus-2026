create database Student1;
--students( student_id INT, name VARCHAR(50), department VARCHAR(30), year INT, marks INT )
create table students(
 student_id INT,
 name VARCHAR(50),
 department VARCHAR(30),
 year INT,
 marks INT
);

insert into students values
(1,'Het','CSE','4','95'),
(2,'Henil','IT','3','78'),
(3,'Parth','CSE','4','90'),
(4,'Meet','CE','3','75'),
(5,'Taksh','CE','4','70'),
(6,'Sanjay','IT','3','60');

--Tasks Count total number of students 
select count(*) as total_students from students;
--Find average marks of students 
select avg(marks) as average_marks from students;
--Find highest and lowest marks 
select max(marks) as highest_marks, min(marks) as lowest_marks from students
--Find department-wise average marks 
select department, avg(marks) as average_marks from students group by department;
--Display departments where average marks > 70	
select department, avg(marks) as average_marks from students
group by department
HAVING AVG(marks) >70;