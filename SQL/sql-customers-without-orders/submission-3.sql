-- Write your query below
SELECT name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    where c.id = o.customer_id

)