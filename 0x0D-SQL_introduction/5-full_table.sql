-- Get the full description of the first_table from the given database
SELECT COLUMN_NAME, 
       COLUMN_TYPE, 
       IS_NULLABLE, 
       COLUMN_DEFAULT, 
       EXTRA 
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' 
  AND table_name = 'first_table';
