#가장 많이 영화 본 user -> count partition by user_id
#2020-feb에 가장 평이 좋은 영화

WITH cte AS (
    SELECT user_id, COUNT(*) AS cnt
    FROM MovieRating
    GROUP BY user_id),

cte2 AS (
    SELECT movie_id, AVG(rating) AS mean
    FROM MovieRating
    WHERE created_at >= '2020-02-01' AND created_at < '2020-03-01'
    GROUP BY movie_id
)
(SELECT u.name AS results
FROM cte c
LEFT JOIN Users u
ON c.user_id = u.user_id
WHERE cnt = (SELECT MAX(cnt) FROM cte)
ORDER BY u.name
LIMIT 1)

UNION ALL 

(SELECT m.title
FROM cte2 d
LEFT JOIN Movies m
ON d.movie_id = m.movie_id
WHERE mean = (SELECT MAX(mean) FROM cte2)
ORDER BY m.title
LIMIT 1)
