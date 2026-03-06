WITH cte AS (SELECT *, SUM(weight) OVER (ORDER BY turn) AS total
FROM Queue)

SELECT person_name 
FROM cte
WHERE total <= 1000
ORDER BY turn DESC
LIMIT 1
