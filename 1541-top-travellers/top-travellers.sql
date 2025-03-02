# Write your MySQL query statement below
select users.name, IFNULL(SUM(rides.distance), 0) as travelled_distance
from users
left join rides on users.id = rides.user_id
GROUP BY users.id
order by 2 DESC, 1 ASC;