SELECT today.id
FROM Weather yesterday
CROSS JOIN Weather today
WHERE today.recordDate - yesterday.recordDate = 1 AND today.temperature > yesterday.temperature