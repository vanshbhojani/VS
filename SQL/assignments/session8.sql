-- 1. Create two tables in your SQL database: Users (user_id, username, city) and Orders 
-- (order_id, user_id, product, amount). Insert at least 3 users and 5 orders, making sure some users have no orders.

use dc_;

create table users(
	user_id int primary key,
    username varchar(50),
    city varchar(20)
);

create table orders(
	order_id int primary key,
    user_id int,
    product varchar(50),
    amount decimal
);

INSERT INTO Users (user_id, username, city)
VALUES
(1, 'Vansh', 'Ahmedabad'),
(2, 'Rahul', 'Surat'),
(3, 'Amit', 'Vadodara'),
(4, 'Priya', 'Rajkot');


INSERT INTO Orders (order_id, user_id, product, amount)
VALUES
(101, 1, 'Laptop', 55000.00),
(102, 1, 'Mouse', 800.00),
(103, 2, 'Keyboard', 1500.00),
(104, 2, 'Monitor', 12000.00),
(105, 3, 'Headphones', 2500.00);

select u.user_id,o.order_id,o.user_id
from users u
left join orders o
on u.user_id=o.user_id;

-- 2. Write an SQL query using INNER JOIN to list all usernames and their ordered products, showing only users who have placed at least one order.

select u.username,o.product
from users u
inner join orders o 
on u.user_id = o.user_id;

-- 3. Write an SQL query using LEFT JOIN to display all usernames along with their ordered products. For users who haven't placed any orders, show NULL for the product.

select u.username,o.order_id 
from users u 
left join orders o 
on u.user_id = o.user_id
where o.order_id is null;

-- 4. Write an SQL query using RIGHT JOIN to show all orders and the corresponding username for each order. If an order has a user_id that doesn't exist in the Users 
-- table, display NULL for the username.<br><br><em><strong>Hint:</strong> Try deleting one user and keeping their order to test this case.</em>

select u.username,o.order_id ,o.user_id,o.product,o.amount
from  users u
right join  orders o
on u.user_id = o.user_id;

delete from users where user_id = 1;


-- 5. Suppose you want to analyze food delivery data like Zomato. Create a CustomerSegments table (segment_id, segment_name), and link it 
-- to Users with a foreign key. Write an SQL query to show each username, their segment name, and total order amount (use JOINs as needed).

ALTER TABLE Users
ADD COLUMN segment_id INT;

CREATE TABLE CustomerSegments (
    segment_id INT PRIMARY KEY,
    segment_name VARCHAR(100)
);

INSERT INTO CustomerSegments (segment_id, segment_name)
VALUES
(2, 'Regular'),
(3, 'New Customer'),
(4, 'regular');

select * from CustomerSegments;

alter table users 
add constraint fk_user_segment
foreign key(segment_id)
references customerSegments(segment_id);

UPDATE Users
SET segment_id = 1
WHERE user_id = 1;

UPDATE Users
SET segment_id = 2
WHERE user_id = 2;

UPDATE Users
SET segment_id = 3
WHERE user_id = 3;

UPDATE Users
SET segment_id = 2
WHERE user_id = 4;

select * from users;

select u.username,cs.segment_name,coalesce(sum(o.amount),0) as total_amount
from users u 
inner join customerSegments cs 
on cs.segment_id = u.segment_id
left join orders o
on u.user_id = o.user_id
group by u.user_id,u.username,cs.segment_name;









