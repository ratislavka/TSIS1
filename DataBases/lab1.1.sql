-- 1. Create database «lab1»
SELECT 'CREATE DATABASE lab1'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'lab1');


-- Connect to the newly created database
\c lab1;

-- 2. Create table «users»
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL
);

-- 3. Add integer column «isadmin» to «users» table
ALTER TABLE users
ADD COLUMN isadmin INT DEFAULT 0;

-- Adding constraint to «isadmin» to 0 or 1
--ALTER TABLE users
--ADD CONSTRAINT isadmin_check CHECK (isadmin IN (0, 1));


-- 4. Type of «isadmin» column to boolean
ALTER TABLE users
ALTER COLUMN isadmin SET DATA TYPE BOOLEAN USING isadmin::BOOLEAN;


-- 5. Set default value as false to «isadmin» column
ALTER TABLE users
ALTER COLUMN isadmin SET DEFAULT FALSE;

-- 6. Add primary key constraint to id column (already done with SERIAL in step 2)
-- ALTER TABLE users
-- ADD CONSTRAINT users_pkey PRIMARY KEY (id);

-- 7. Create table «tasks»
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    user_id INT
);

-- 8. Delete «tasks» table
DROP TABLE IF EXISTS tasks;

DROP TABLE IF EXISTS users;

-- 9. Delete «lab1» database (Execute with caution!)
\c postgres  -- Connect to the default 'postgres' database before dropping
DROP DATABASE IF EXISTS lab1;