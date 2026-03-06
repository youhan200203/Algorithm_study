SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
LEFT JOIN Logs b
ON a.num = b.num AND a.id = b.id + 1
LEFT JOIN Logs c
ON b.num = c.num AND b.id = c.id + 1
WHERE b.num IS NOT NULL AND c.num IS NOT NULL