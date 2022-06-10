/*
1. Write a query to display for each order, the account ID, total 
amount of the order, and the level of the order - ‘Large’ or ’Small’ - 
depending on if the order is $3000 or more, or smaller than $3000.
*/

SELECT CASE
		WHEN total_amt_usd > 3000 THEN 'large'
        WHEN total_amt_usd < 3000 THEN 'small'
        END AS level_of_orders, ord.total_amt_usd, a.id 
FROM orders ord
JOIN accounts a
ON ord.account_id = a.id
LIMIT 10;

/*
2. Write a query to display the number of orders in each of three categories, 
based on the total number of items in each order. The three categories are: 
'At Least 2000', 'Between 1000 and 2000' and 'Less than 1000'.
*/

SELECT COUNT(id), CASE WHEN total >= 2000 THEN 'At least 2000'
        WHEN total BETWEEN 1000 AND 2000 THEN 'Between 1000 and 2000'
        WHEN total < 1000 THEN 'Less than 1000' END AS level_of_orders
FROM orders
GROUP BY 2;

/*
3. We would like to understand 3 different levels of customers based on the
amount associated with their purchases. The top level includes anyone with
a Lifetime Value (total sales of all orders) greater than 200,000 usd. 
The second level is between 200,000 and 100,000 usd. The lowest level 
is anyone under 100,000 usd. Provide a table that includes the level 
associated with each account. You should provide the  account name, 
the total sales of all orders for the customer, and the level. Order
with the top spending customers listed first.
*/

SELECT a.name, SUM(ord.total_amt_usd) AS sum_total_amt, CASE
        WHEN SUM(ord.total_amt_usd) > 200000 THEN 'top level'
        WHEN SUM(ord.total_amt_usd) BETWEEN 100000 AND 200000 THEN 'mid level'
        WHEN SUM(ord.total_amt_usd) < 100000 THEN 'low level' END AS customer_level
FROM accounts AS a
JOIN orders AS ord
ON a.id = ord.account_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

/*
4. We would now like to perform a similar calculation to the first, but 
we want to obtain the total amount spent by customers only in 2016 and 2017. 
Keep the same levels as in the previous question. Order with the top 
spending customers listed first.
*/

SELECT a.name, DATE_PART('year', ord.occurred_at) AS year, SUM(ord.total_amt_usd) AS sum_total_amt, CASE
        WHEN SUM(ord.total_amt_usd) > 200000 THEN 'top level'
        WHEN SUM(ord.total_amt_usd) BETWEEN 100000 AND 200000 THEN 'mid level'
        WHEN SUM(ord.total_amt_usd) < 100000 THEN 'low level' END AS customer_level
FROM accounts AS a
JOIN orders AS ord
ON a.id = ord.account_id
WHERE DATE_PART('year', ord.occurred_at) = 2016 OR DATE_PART('year', ord.occurred_at) =2017
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 10;

/*
5. We would like to identify top performing sales reps, which are sales reps 
associated with more than 200 orders. Create a table with the sales rep name, 
the total number of orders, and a column with top or not depending on if 
they have more than 200 orders. Place the top sales people first in your 
final table.
*/

SELECT sr.name, COUNT(ord.total) no_of_sales, CASE
        WHEN COUNT(ord.total) > 200 THEN 'top'
        ELSE 'low' END AS top_customers
FROM orders ord
JOIN accounts a
ON ord.account_id = a.id
JOIN sales_reps sr
ON a.sales_rep_id = sr.id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

/*
The previous didn't account for the middle, nor the dollar amount associated 
with the sales. Management decides they want to see these characteristics 
represented as well. We would like to identify top performing sales reps, 
which are sales reps associated with more than 200 orders or more than 
750000 in total sales. The middle group has any rep with more than 150 
orders or 500000 in sales. Create a table with the sales rep name, the total 
of orders, total sales across all orders, and a column with top, middle, 
or low depending on this criteria. Place the top sales people based on 
dollar amount of sales first in your final table. You might see a few 
upset sales people by this criteria!
*/
SELECT sr.name, COUNT(ord.total), SUM(ord.total_amt_usd), CASE
        WHEN COUNT(ord.total) > 200 OR SUM(ord.total_amt_usd) > 750000 THEN 'top'
        WHEN COUNT(ord.total) > 150 OR SUM(ord.total_amt_usd) > 500000 THEN 'middle'
        ELSE 'low' END AS customer_level
FROM orders ord
JOIN accounts a
ON ord.account_id = a.id
JOIN sales_reps sr
ON a.sales_rep_id = sr.id
GROUP BY 1
ORDER BY 3 DESC;


--LESSON FOUR 
SELECT channel, AVG(no_of_events)
FROM (SELECT DATE_TRUNC('day', wb.occurred_at), 
        channel, COUNT(id) no_of_events
      FROM web_events wb
      GROUP BY 1,2
      ORDER BY 1) sub
GROUP BY 1;



SELECT *
FROM (SELECT DATE_TRUNC('day',wb.occurred_at), 
        channel, COUNT(id) no_of_events
        FROM web_events wb
        GROUP BY 1,2
        ORDER BY 1) sub 
ORDER BY no_of_events DESC 
LIMIT 10;

/*
SELECT AVG(standard_qty) avg_std_qty, AVG(gloss_qty) avg_gloss_qty,
           AVG(poster_qty) avg_poster_qty, DATE_TRUNC('year', occurred_at)
                    FROM orders
GROUP BY 4
ORDER BY 4;
*/
;

SELECT DATE_TRUNC('month', occurred_at) , AVG(standard_qty) avg_std_qty,
           AVG(gloss_qty) avg_gloss_qty,
           AVG(poster_qty) avg_poster_qty,
           SUM(total_amt_usd)
FROM orders
WHERE DATE_TRUNC('month', occurred_at) = 
    (SELECT DATE_TRUNC('month', MIN(occurred_at)) months
    FROM orders)
GROUP BY 1
ORDER BY 1
LIMIT 10;
-- HAVING occurred_at = (SELECT DATE_TRUNC('month', MIN(occurred_at)) months
  --                  FROM orders);

/* The average amount of standard paper sold on the first month that any order was 
placed in the orders table (in terms of quantity). */

SELECT occurred_at, standard_qty
FROM orders
WHERE DATE_TRUNC('month', occurred_at) = 
                    (SELECT DATE_TRUNC('month', MIN(occurred_at)) months
    FROM orders)
ORDER BY 1
LIMIT 5;

--SUBQUERY MANIA
/*1. Provide the name of the sales_rep in each region with the largest amount of 
total_amt_usd sales.*/
SELECT sr.name, r.name, SUM(ord.total_amt_usd)
FROM sales_reps sr
JOIN region r
ON sr.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = sr.id
JOIN orders ord
ON a.id = ord.account_id
GROUP BY 2, 1
ORDER BY 3 DESC
LIMIT 5;

/*2. For the region with the largest (sum) of sales total_amt_usd, how many total 
(count) orders were placed? */
SELECT r.name, SUM(ord.total) total_qty, SUM(ord.total_amt_usd) total_amt
FROM region r
JOIN sales_reps sr
ON sr.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = sr.id
JOIN orders ord
ON ord.account_id = a.id
GROUP BY 1
ORDER BY 3 DESC;

/*3. How many accounts had more total purchases than the account name which has bought 
the most standard_qty paper throughout their lifetime as a customer?*/
SELECT SUM(ord.standard_qty) no_of_std
        FROM accounts a
        JOIN orders ord 
        ON a.id = ord.account_id
        GROUP BY a.name
        ORDER BY 1 DESC
        LIMIT 1;

SELECT a.name
FROM accounts a
WHERE a.id =
        (SELECT a.id
        FROM orders
        ORDER BY standard_qty DESC
        LIMIT 1)
LIMIT 1;

SELECT SUM(ord.total), SUM(ord.standard_qty) no_of_std
        FROM accounts a
        JOIN orders ord 
        ON a.id = ord.account_id
        GROUP BY a.name
        ORDER BY 1 DESC
        LIMIT 5;

SELECT COUNT(a.name), ord.total 
FROM accounts a
JOIN orders ord
ON a.id = ord.account_id
WHERE ord.total =
        (SELECT SUM(ord.standard_qty) no_of_std
        FROM accounts a
        JOIN orders ord 
        ON a.id = ord.account_id
        GROUP BY a.name
        ORDER BY 1 DESC
        LIMIT 1)
GROUP BY 2;

/*4. For the customer that spent the most (in total over their lifetime as a customer) 
total_amt_usd, how many web_events did they have for each channel?*/
SELECT a.name, SUM(ord.total_amt_usd)
FROM accounts a  
JOIN orders ord
ON a.id = ord.account_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

SELECT id, total, (SELECT AVG(total) FROM orders)
FROM orders;




