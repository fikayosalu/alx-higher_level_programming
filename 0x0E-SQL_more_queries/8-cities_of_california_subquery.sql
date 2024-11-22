-- A script that creates the database hbtn_0d_usa and the table cities 
-- (in the database hbtn_0d_usa) on your MySQL server.
USE hbtn_0d_usa;

SELECT cities.name
FROM cities, states
WHERE states.name = 'California'
  AND cities.state_id = states.id
ORDER BY cities.id ASC;
