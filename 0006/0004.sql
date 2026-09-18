SELECT confidence, COUNT(*) AS n
FROM endpoints
GROUP BY confidence
ORDER BY n DESC;