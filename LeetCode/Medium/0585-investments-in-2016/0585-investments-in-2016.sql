#tiv_2016의 sum when tiv_2015가 같은 또다른 pid가 있고 lat,lon이 unique

WITH cte AS (
    SELECT a.pid, a.tiv_2016
    FROM Insurance a
    LEFT JOIN Insurance b
    ON a.tiv_2015 = b.tiv_2015 AND a.pid != b.pid
    WHERE b.pid IS NOT NULL
    GROUP BY a.pid
),

cte2 AS (
    SELECT pid, tiv_2015, tiv_2016 
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)

SELECT ROUND(SUM(c.tiv_2016), 2) AS tiv_2016
FROM cte2 c
JOIN cte d
ON c.pid = d.pid