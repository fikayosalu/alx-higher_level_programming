-- Convert the hbtn_0c_0 database to UTF8 (utf8mb4, utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the first_table to UTF8 (utf8mb4, utf8mb4_unicode_ci)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name column in first_table to UTF8 (utf8mb4, utf8mb4_unicode_ci)
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
