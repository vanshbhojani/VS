-- 1. Write an SQL query to display the total number of orders placed by each user in a 'food_orders' table, grouped by user_id.

select * 
from food_orders
group by order_id;


-- 2. Using a 'transactions' table with columns (transaction_id, user_id, amount, payment_method), write an SQL query to show the total amount spent by each payment_method.

select sum(amount) as total_amount,payment_method 
from transactions
group by payment_mathod;


-- 3. Given a 'movies' table with columns (movie_id, genre, box_office_collection), write an SQL query to display each genre and its total box_office_collection, but
-- only show genres where the total collection is above 10 crore.<br><br><em><strong>Hint:</strong> Use GROUP BY and HAVING together to filter the aggregated results.</em>

select genre , sum(box_office_collection) as sum_box_coll
from movies
group by genre
having sum(box_office_collection)>10;

-- 4. Suppose you have a 'playlist' table with columns (playlist_id, user_id, song_id, duration). Write an SQL query to find users who have created playlists with a 
-- combined song duration of more than 2 hours (7200 seconds), showing user_id and total duration.

select user_id, sum(duration) as song_duration
from playlist
group by user_id
having sum(duration)>7200;















