-- Write your PostgreSQL query statement below
SELECT x, y, z, (
    CASE WHEN x + y > z AND y + z > x AND z + x > y 
        THEN 'YES' 
        ELSE 'NO'
     END) AS triangle
FROM Triangle