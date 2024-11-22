-- A script that creates the table unique_id on your MySQL server
-- id INT with the default value 1 and must be unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT PRIMARY KEY DEFAULT 1,
	name VARCHAR(256)
);
