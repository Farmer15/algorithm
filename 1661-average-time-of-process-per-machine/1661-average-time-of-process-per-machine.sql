-- Write your PostgreSQL query statement below
    SELECT machine_id, ROUND(AVG(sum_time)::numeric, 3) AS processing_time
    FROM (
        SELECT machine_id, (
        CASE 
            WHEN activity_type = 'start' THEN -sum(timestamp)
            WHEN activity_type = 'end' THEN sum(timestamp)
            END
        ) AS sum_time
            FROM Activity
            GROUP BY machine_id, activity_type
        )
    GROUP BY machine_id