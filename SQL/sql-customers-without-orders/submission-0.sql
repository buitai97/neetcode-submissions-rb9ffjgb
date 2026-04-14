-- Write your query below
SELECT name
FROM customers
WHERE NOT EXISTS (
    SELECT *
    FROM orders
    where customers.id = orders.customer_id

)