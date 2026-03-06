#LEFT JOIN하면 될 거 같은뎅? a.id = b.p_id가 되면 a가 null이면 a를 p_id로 가지는 게 없다는 거니까 자식

SELECT a.id, (CASE WHEN SUM(a.p_id) IS NULL THEN 'Root' WHEN SUM(b.id) IS NULL THEN 'Leaf' ELSE 'Inner' END) AS 'type'
FROM Tree a
LEFT JOIN Tree b
ON a.id = b.p_id
GROUP BY a.id