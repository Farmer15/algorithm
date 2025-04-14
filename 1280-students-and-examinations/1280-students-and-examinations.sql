SELECT S.student_id, S.student_name, S.subject_name, (
    CASE WHEN E.count IS NULL THEN 0
    ELSE E.count
    END
) AS attended_exams
FROM (SELECT * 
FROM Students
CROSS JOIN Subjects
ORDER BY student_id) AS S
FULL OUTER JOIN (SELECT student_id, subject_name, count(subject_name)
FROM Examinations
GROUP BY student_id, subject_name) AS E
ON S.student_id = E.student_id AND S.subject_name = E.subject_name
ORDER BY student_id, S.subject_name ASC 
