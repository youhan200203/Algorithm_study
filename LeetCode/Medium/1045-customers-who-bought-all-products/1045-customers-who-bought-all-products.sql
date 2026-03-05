WITH cte AS 
(SELECT DISTINCT customer_id, product_key FROM Customer),

cte2 AS 
(SELECT customer_id, COUNT(DISTINCT product_key) AS cnt FROM cte GROUP BY customer_id)

SELECT customer_id
FROM cte2
WHERE cnt = (SELECT COUNT(*) FROM Product)
