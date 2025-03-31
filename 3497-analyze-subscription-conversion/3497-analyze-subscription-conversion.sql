-- Write your PostgreSQL query statement below
SELECT user_id, 
ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS trial_avg_duration, 
ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END), 2) AS paid_avg_duration
FROM UserActivity
WHERE user_id IN (SELECT user_id FROM UserActivity WHERE activity_type = 'paid') AND activity_type != 'cancelled'
GROUP BY user_id
ORDER BY user_id