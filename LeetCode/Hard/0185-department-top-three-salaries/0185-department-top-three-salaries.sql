#같은 salary일 때 같이 취급이므로 DENSE_RANK를 써야함

WITH cte AS (SELECT *, DENSE_RANK() OVER (PARTITION BY departmentID ORDER BY salary DESC) AS rnk
FROM Employee)

SELECT d.name AS Department, c.name AS Employee, salary AS Salary
FROM Department d
LEFT JOIN cte c
ON c.departmentId = d.id
WHERE rnk in (1, 2, 3)
