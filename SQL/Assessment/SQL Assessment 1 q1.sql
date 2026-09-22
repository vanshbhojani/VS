create database Assessment;
use Assessment;

-- Create the Worker table
CREATE TABLE Worker (
    WORKER_ID INT PRIMARY KEY,
    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    SALARY INT,
    JOINING_DATE DATETIME,
    DEPARTMENT VARCHAR(50)
);

-- Insert the data from the image
INSERT INTO Worker (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) 
VALUES
    (1, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
    (2, 'Niharika', 'Verma', 80000, '2014-06-11 09:00:00', 'Admin'),
    (3, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
    (4, 'Amitabh', 'Singh', 500000, '2014-02-20 09:00:00', 'Admin'),
    (5, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
    (6, 'Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
    (7, 'Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
    (8, 'Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');
    
select * from worker;

-- 1. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME
-- Ascending and DEPARTMENT Descending. 

select * from worker order by FIRST_NAME asc;

select * from worker order by FIRST_NAME desc;

-- 2.Write an SQL query to print details for Workers with the first names “Vipul” and “Satish”
-- from the Worker table. 

select * from worker 
where FIRST_NAME in ("Vipul","Satish");

-- 3. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and
-- contains six alphabets. 

select * from worker where FIRST_NAME like '%h';

-- 4. Write an SQL query to print details of the Workers whose SALARY lies between 1.  

select * from worker where salary between 100000 and 500000;

-- 5. Write an SQL query to fetch duplicate records having matching data in some fields of a table.

SELECT FIRST_NAME, DEPARTMENT, COUNT(*)
FROM worker
GROUP BY FIRST_NAME , DEPARTMENT
HAVING COUNT(*) > 1;

-- 6. Write an SQL query to show the top 6 records of a table. 

select * from worker order by  salary desc limit 6;

-- 7. Write an SQL query to fetch the departments that have less than five people in them. 

SELECT FIRST_NAME, DEPARTMENT
FROM Worker
WHERE DEPARTMENT IN (
    SELECT DEPARTMENT
    FROM Worker
    GROUP BY DEPARTMENT
    HAVING COUNT(WORKER_ID) < 3
);

-- 8. Write an SQL query to show all departments along with the number of people in there. 

SELECT DEPARTMENT, COUNT(WORKER_ID) as NumberOfWorkers
FROM Worker
GROUP BY DEPARTMENT;


-- 9. Write an SQL query to print the name of employees having the highest salary in each
-- department

select FIRST_NAME , salary ,department 
from worker 
where (department, salary) in (
	select department, max(salary)
    from worker 
    group by department
);