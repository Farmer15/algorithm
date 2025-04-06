-- Write your PostgreSQL query statement below
SELECT 
(
    CASE 
        WHEN Employees.employee_id is NULL THEN Salaries.employee_id
        WHEN Salaries.employee_id is NULL THEN Employees.employee_id
    END
) AS employee_id
FROM Employees
FULL OUTER JOIN Salaries
ON Employees.employee_id = Salaries.employee_id
WHERE Employees.employee_id is NULL OR Salaries.employee_id is NULL