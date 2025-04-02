-- Write your PostgreSQL query statement below
SELECT id,
sum(CASE WHEN month = 'Jan' THEN revenue ELSE NULL END) AS Jan_Revenue,
sum(CASE WHEN month = 'Feb' THEN revenue ELSE NULL END) AS Feb_Revenue,
sum(CASE WHEN month = 'Mar' THEN revenue ELSE NULL END) AS Mar_Revenue,
sum(CASE WHEN month = 'Apr' THEN revenue ELSE NULL END) AS Apr_Revenue,
sum(CASE WHEN month = 'May' THEN revenue ELSE NULL END) AS May_Revenue,
sum(CASE WHEN month = 'Jun' THEN revenue ELSE NULL END) AS Jun_Revenue,
sum(CASE WHEN month = 'Jul' THEN revenue ELSE NULL END) AS Jul_Revenue,
sum(CASE WHEN month = 'Aug' THEN revenue ELSE NULL END) AS Aug_Revenue,
sum(CASE WHEN month = 'Sep' THEN revenue ELSE NULL END) AS Sep_Revenue,
sum(CASE WHEN month = 'Oct' THEN revenue ELSE NULL END) AS Oct_Revenue,
sum(CASE WHEN month = 'Nov' THEN revenue ELSE NULL END) AS Nov_Revenue,
sum(CASE WHEN month = 'Dec' THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department
GROUP BY id