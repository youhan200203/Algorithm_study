#LEFT JOIN하면 될 거 같은뎅? a.id = b.p_id가 되면 a가 null이면 a를 p_id로 가지는 게 없다는 거니까 자식

SELECT id, CASE WHEN p_id IS NULL THEN 'Root' WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner' ELSE 'Leaf' END AS 'type'
FROM Tree