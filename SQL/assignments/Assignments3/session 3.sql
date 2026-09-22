use restaurants;

select * from restaurants;

-- 1. Write an SQL query to select all restaurants from a table named 'restaurants' where the rating is greater than or equal to 4.5.
select * from restaurants where rating >4.5;

-- 2. In a table called 'movies', filter and display only the movies released after 2020 and with genre 'Action' using the WHERE clause and AND operator.
use moviesdb;
select * from movies;

select * from movies where release_year = 2022;

-- 3. Given a table 'products' with columns (id, name, price, category), write a query to find all products not in the 'Electronics' category or with a price less than 500.
use salse;

create table Products(
	id int primary key,
    name varchar(50),
    price int,
    category varchar(50)
);
 
INSERT INTO Products (id, name, price, category)
VALUES
(1, 'Laptop', 55000, 'Electronics'),
(2, 'Smartphone', 25000, 'Electronics'),
(3, 'Headphones', 1500, 'Electronics'),
(4, 'Keyboard', 800, 'Electronics'),
(5, 'Mouse', 500, 'Electronics'),
(6, 'Monitor', 12000, 'Electronics'),
(7, 'Office Chair', 7500, 'Furniture'),
(8, 'Study Table', 6000, 'Furniture'),
(9, 'Bookshelf', 4500, 'Furniture'),
(10, 'Notebook', 150, 'Stationery'),
(11, 'Pen Set', 250, 'Stationery'),
(12, 'Backpack', 1200, 'Accessories'),
(13, 'Water Bottle', 400, 'Accessories'),
(14, 'Watch', 3500, 'Accessories'),
(15, 'Shoes', 2800, 'Fashion'),
(16, 'T-Shirt', 700, 'Fashion'),
(17, 'Jeans', 1800, 'Fashion'),
(18, 'Coffee Maker', 4500, 'Appliances'),
(19, 'Mixer Grinder', 3200, 'Appliances'),
(20, 'Table Lamp', 900, 'Home Decor');

SELECT *
FROM products
WHERE category <> 'Electronics'
   OR price < 500;

-- 4. Write an SQL query for a table 'users' to show all users who are NOT from 'Ahmedabad' and have more than 1000 followers.<br><br><em><strong>Hint:</strong>
-- Use the NOT operator combined with AND.</em> 

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    followers INT
);

INSERT INTO users (id, name, city, followers)
VALUES
(1, 'Vansh', 'Ahmedabad', 1500),
(2, 'Rahul', 'Mumbai', 2500),
(3, 'Priya', 'Ahmedabad', 800),
(4, 'Amit', 'Delhi', 1200),
(5, 'Neha', 'Surat', 950),
(6, 'Karan', 'Pune', 1800),
(7, 'Riya', 'Ahmedabad', 2200),
(8, 'Jay', 'Vadodara', 1100);

select * from users;

select * from users where NOT city= 'Ahmedabad' and followers >1000;








 
 