-- Write your PostgreSQL query statement below


SELECT EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI
  FULL OUTER JOIN Employees
  ON EmployeeUNI.id = Employees.id
  WHERE NOT Employees.name is NULL