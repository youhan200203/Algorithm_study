WITH cte AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
)

SELECT id, COUNT(*) AS num
FROM cte
GROUP BY id
HAVING num >= ALL (
    SELECT COUNT(*)
    FROM cte
    GROUP BY id
)