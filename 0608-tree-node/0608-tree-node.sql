-- Write your PostgreSQL query statement below
SELECT DISTINCT t1.id, (
    CASE 
        WHEN t1.p_id is Null THEN 'Root'
        WHEN t2.p_id is Null THEN 'Leaf'
        ELSE 'Inner'
    END) AS type
FROM Tree t1
LEFT OUTER JOIN Tree t2
ON t1.id = t2.p_id


