SELECT teacher_id, count(subject_id) AS cnt FROM (SELECT DISTINCT teacher_id, subject_id FROM Teacher)
GROUP BY teacher_id
ORDER BY teacher_id