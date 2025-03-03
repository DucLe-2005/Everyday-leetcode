select v.customer_id as customer_id, count(*) as count_no_trans
from visits v
where v.visit_id NOT IN (
    select visit_id
    from transactions
)
group by customer_id;