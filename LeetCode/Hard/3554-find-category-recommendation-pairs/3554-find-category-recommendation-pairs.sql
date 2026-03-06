#두 개의 카테고리를 둘다 산 고객 수와 그 갯수를 구해야 함
#product_id가 아니라 카테고리로 해야 함

WITH cte AS (SELECT p.user_id, p.product_id, i.category
FROM ProductPurchases p
LEFT JOIN ProductInfo i
ON p.product_id = i.product_id)

SELECT a.category AS category1, b.category AS category2, COUNT(DISTINCT a.user_id) AS customer_count
FROM cte a
JOIN cte b
ON a.user_id = b.user_id AND a.category < b.category
GROUP BY a.category, b.category
HAVING COUNT(DISTINCT a.user_id) >= 3
ORDER BY customer_count DESC, category1, category2