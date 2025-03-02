SELECT e.employee_id 
FROM employees e
WHERE employee_id NOT IN (SELECT employee_id FROM salaries)

UNION

SELECT s.employee_id
FROM salaries s
WHERE employee_id NOT IN (SELECT employee_id FROM employees)

ORDER BY employee_id