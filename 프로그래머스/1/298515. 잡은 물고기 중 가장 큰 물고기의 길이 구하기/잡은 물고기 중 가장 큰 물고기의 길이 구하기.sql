SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM FISH_INFO
GROUP BY FISH_TYPE 
ORDER BY MAX_LENGTH DESC
LIMIT 1;