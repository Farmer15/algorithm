-- Write your PostgreSQL query statement below
SELECT id, (
    CASE WHEN id % 2 = 0 THEN prev
         ELSE next
         END
) AS student
FROM (
    SELECT 
        id, student,
        LAG(student, 1, student) OVER (ORDER BY id) AS prev,
        LEAD(student, 1, student) OVER (ORDER BY id) AS next
    FROM Seat
    )