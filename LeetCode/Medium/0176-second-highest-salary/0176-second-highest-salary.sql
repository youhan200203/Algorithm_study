#RANK?
WITH cte AS (SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
FROM Employee)

SELECT MAX(DISTINCT salary) AS SecondHighestSalary
FROM cte 
WHERE rnk = 2
