SELECT 
    query_name, 
    ROUND(avg(rating/position) ,2) AS quality, 
    ROUND((sum(case when rating < 3 then 1 else 0 end)*100/count(rating)),2) as poor_query_percentage
FROM
    Queries
GROUP BY
    query_name