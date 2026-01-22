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
--Display all student records
Select * from students;
--Display only name and department
Select name, department from students;
--Find students with marks greater than 75
select * from students where marks > 75;
--Display students from CSE department
select * from students where department = 'CSE';
--Sort students by marks (descending)
select * from students order by marks desc;
--Display top 3 scorers	
select top 3 * from students order by marks desc
	