SELECT a.id, IFNULL((CASE WHEN a.id % 2 = 1 THEN c.student ELSE b.student END), a.student) AS student
FROM Seat a
LEFT JOIN Seat b
ON a.id = b.id + 1
LEFT JOIN Seat c
ON a.id = c.id - 1
