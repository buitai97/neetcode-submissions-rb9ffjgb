-- Write your query below
SELECT
    employee_id, 
    CASE
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' then salary
        ELSE 0
    end as bonus
from employees
ORDER BY employee_id;
