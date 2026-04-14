-- Write your query below
SELECT name
FROM customers
WHERE NOT EXISTS (
    SELECT 1
    FROM orders
    where customers.id = orders.customer_id

)