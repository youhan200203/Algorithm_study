#각 계절별로 가장 갯수가 많이 팔린 category를 찾아야함
#즉 product_id에 cateogry left join
#CASE WHEN MONTH(sale_date)으로 계절 나누고
#GROUP BY 계절, sum(quantity), total revenue 구하기

WITH cte AS (SELECT CASE WHEN MONTH(SALE_DATE) IN (12, 1, 2) THEN 'Winter' WHEN MONTH(SALE_DATE) IN (3, 4, 5) THEN 'Spring' WHEN MONTH(SALE_DATE) IN (6, 7, 8) THEN 'Summer' ELSE 'Fall' END AS season, category, SUM(quantity) AS total_quantity, SUM(price*quantity) AS total_revenue
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY season, category),

cte2 AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC, category) AS rnk
FROM cte)

SELECT season, category, total_quantity, total_revenue
FROM cte2
WHERE rnk = 1