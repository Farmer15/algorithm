-- Write your PostgreSQL query statement below
SELECT name, bonus
FROM Employee
LEFT OUTER JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE bonus <= 1000 or bonus is Null
