use restaurants;

select * from restaurants;

-- Write an SQL query to find all restaurants in a table called Restaurants whose names end with 'Cafe' using the LIKE operator.

SELECT *
FROM Restaurants
WHERE name LIKE '%Cafe';

SET SQL_SAFE_UPDATES = 0;

-- 2. In a Flipkart-style Products table, use the BETWEEN operator to select all products with a price between 500 and 1500 rupees.

select product ,price 
from Flipkart-style
where price  between 500 and 15000;

-- 3. Write an SQL query to display all users from a Users table whose city is either 'Ahmedabad', 'Surat', or 'Vadodara' using the IN operator.

select users, city 
from custemers
where city in ('Ahmedabad','surat','vadodara');

-- 4. Given a table called Songs with columns song_name and artist_name, find all songs where the artist_name contains the letter sequence 'ar' anywhere in the name using the LIKE operator.
-- <br><br><em><strong>Hint:</strong> Use wildcards on both sides of the pattern.</em>

select song_name,artist_name 
from Songs
where song_name like '%ar%';



