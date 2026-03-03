SELECT name
FROM Employee
WHERE id in (SELECT managerId
FROM Employee
GROUP BY managerID
HAVING COUNT(managerId) >= 5)