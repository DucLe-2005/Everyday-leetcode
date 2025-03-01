# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN
    (
        SELECT o.sales_id
        FROM Orders o
        LEFT JOIN company c ON c.com_id = o.com_id
        WHERE c.name = 'RED'
    );