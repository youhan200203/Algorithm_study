#free_trail -> paid
#free trial 동안 duration 평균
#where activity_type = 'free_trial' group by user_id

SELECT user_id, ROUND(SUM(CASE WHEN activity_type = 'free_trial' THEN activity_duration ELSE 0 END)/SUM(activity_type = 'free_trial'), 2) AS trial_avg_duration, ROUND(SUM(CASE WHEN activity_type = 'paid' THEN activity_duration ELSE 0 END)/SUM(activity_type = 'paid'), 2) AS paid_avg_duration
FROM UserActivity
GROUP BY user_id
HAVING SUM(activity_type = 'paid') > 0