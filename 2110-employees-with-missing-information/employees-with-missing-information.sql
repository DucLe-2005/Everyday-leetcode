SELECT F.employee_id
FROM (
    SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
    UNION
    SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)
)
AS F
WHERE F.salary IS NULL OR F.name IS NULL
ORDER BY F.employee_id;