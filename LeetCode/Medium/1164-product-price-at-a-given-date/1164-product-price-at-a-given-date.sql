WITH cte AS ( 
    SELECT product_id, MAX(change_date) AS new_date 
    FROM Products 
    WHERE change_date <= '2019-08-16' 
    GROUP BY product_id) 

SELECT p.product_id, CASE SUM(CASE WHEN p.change_date = c.new_date THEN new_price ELSE 0 END) WHEN 0 THEN 10 ELSE SUM(CASE WHEN p.change_date = c.new_date THEN new_price ELSE 0 END) END AS price 
FROM Products p 
LEFT JOIN cte c 
ON p.product_id = c.product_id 
GROUP BY p.product_id