# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN
    (
        SELECT o.sales_id
        FROM Orders o
        WHERE o.com_id IN (
            SELECT com_id
            FROM COMPANY c
            WHERE c.name = 'RED'
        )
    );