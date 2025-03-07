SELECT 
    r.contest_id,
    round(count(r.user_id) *100 /(SELECT count(user_id) FROM Users),2) AS percentage
FROM 
    Register r
GROUP BY
    r.contest_id
ORDER BY
    percentage DESC,
    r.contest_id ASC;