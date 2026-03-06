#combination 다른 두 개 product를 산 같은 고객 찾기

WITH cte AS (SELECT a.product_id AS product1_id, b.product_id AS product2_id, COUNT(DISTINCT a.user_id) AS cnt
FROM ProductPurchases a
JOIN ProductPurchases b
ON a.user_id = b.user_id AND a.product_id < b.product_id
GROUP BY a.product_id, b.product_id
HAVING COUNT(DISTINCT a.user_id) >= 3)

SELECT product1_id, product2_id, i.category AS product1_category, i2.category AS product2_category, cnt as customer_count
FROM cte c
LEFT JOIN ProductInfo i
ON c.product1_id = i.product_id
LEFT JOIN ProductInfo i2
ON c.product2_id = i2.product_id
ORDER BY customer_count DESC, product1_id, product2_id