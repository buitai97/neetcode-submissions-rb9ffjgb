-- Write your query below

select c.customer_id, c.customer_name
from customers c
where c.customer_id IN (
    select customer_id FROM orders where product_name = 'A'
)
and c.customer_id IN (
    select customer_id FROM orders where product_name = 'B'
)
and c.customer_id not IN (
    select customer_id FROM orders where product_name = 'C'
)
order by c.customer_name