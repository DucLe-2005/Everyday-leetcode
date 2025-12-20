DELETE FROM Person
WHERE id IN (
    SELECT id
    FROM (
        SELECT p2.id
        FROM Person p1
        LEFT JOIN Person p2
        ON p1.email = p2.email AND p2.id > p1.id
    ) AS tmp
);