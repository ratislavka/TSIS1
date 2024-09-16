-- 1. Create database called «lab1»
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'lab1') THEN
        CREATE DATABASE lab1;
    END IF;
END
$$;

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

-- 4. Type of «isadmin» column to boolean
alter table users
alter column isadmin type boolean using isadmin::boolean;


-- 5. Set default value as false to «isadmin» column
alter table users
alter column isadmin set default false;

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