-- Select score and name from second_table where score is greater than or equal to 10, ordered by score (top first)
SELECT score, name 
FROM second_table 
WHERE score >= 10
ORDER BY score DESC;