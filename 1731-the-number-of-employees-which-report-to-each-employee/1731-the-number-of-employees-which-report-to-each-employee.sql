SELECT E2.employee_id, E2.name, count(E1.name) AS reports_count, round(avg(E1.age)) AS average_age
FROM Employees E1
JOIN Employees E2
ON E1.reports_to = E2.employee_id
WHERE not E1.reports_to is NULL 
GROUP BY E2.employee_id, E2.name
ORDER BY E2.employee_id