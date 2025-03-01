# Write your MySQL query statement below
SELECT name as Customers
FROM customers c
WHERE c.id NOT IN (
    SELECT customerId
    FROM orders
);