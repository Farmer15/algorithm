-- Write your PostgreSQL query statement below
SELECT P.project_id, ROUND(avg(E.experience_years)::numeric, 3) AS average_years FROM Project P
RIGHT OUTER JOIN Employee E
ON P.employee_id = E.employee_id
WHERE NOT P.project_id is NULL
GROUP BY P.project_id
ORDER BY P.project_id