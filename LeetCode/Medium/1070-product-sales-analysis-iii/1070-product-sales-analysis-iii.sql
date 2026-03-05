#rank를 쓰기
#제일 처음 등장한 year를 product_id별로 where 써서 구하기

WITH cte AS (
    SELECT sale_id, product_id, year, quantity, price, RANK() OVER (PARTITION BY product_id ORDER BY year) AS rnk
    FROM Sales 
)

SELECT product_id, year AS first_year, quantity, price
FROM cte
WHERE rnk = 1