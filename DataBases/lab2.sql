-- 1. Create database called «lab2»
CREATE DATABASE IF NOT EXISTS lab2;

-- 2. Create a simple table countries including columns
-- country_id (primary_key, auto increment), country_name(string), region_id(integer) and population(integer).
--USE lab2;
CREATE TABLE IF NOT EXISTS countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL,
    region_id INT,
    population INT
);

-- 3. Insert a row with any data into the table countries against each columns.
INSERT INTO countries (country_id, country_name, region_id, population)
VALUES (1, 'USA', 1, 333300000);

-- 4. Insert one row into the table countries against the column country_id and country_name.
INSERT INTO countries (country_id, country_name)
VALUES (2, 'United Kingdom');

-- 5. Insert NULL value to region_id column for a row of countries table.
INSERT INTO countries (country_id, country_name, region_id, population)
VALUES (3, 'Canada', NULL, 38000000);

-- 6. Insert 3 rows by a single insert statement.
INSERT INTO countries (country_id, country_name, region_id, population)
VALUES
    (4, 'Germany', 2, 83000000),
    (5, 'France', 2, 67000000),
    (6, 'Italy', 2, 60000000);

-- 7. Set default value ‘Kazakhstan’ to country_name column.
ALTER TABLE countries
ALTER COLUMN country_name SET DEFAULT 'Kazakhstan';

-- 8. Insert default value to country_name column for a row of countries table.
INSERT INTO countries (country_id, region_id, population)
VALUES (7, 3, 18000000);

-- 9. Insert only default values against each column of countries table.
INSERT INTO countries (region_id, population)
VALUES (NULL, NULL);

-- 10. Create duplicate of countries table named countries_new with all structure using LIKE keyword.
CREATE TABLE countries_new LIKE countries;

-- 11. Insert all rows from countries table to countries_new table.
INSERT INTO countries_new
SELECT * FROM countries;

-- 12. Change region_id of country to «1» if it equals NULL. (Use WHERE clause and IS NULL operator)
UPDATE countries
SET region_id = 1
WHERE region_id IS NULL;

-- 13. Write a SQL statement to increase population of each country by 10%.
-- Statement should return country_name and updated population column with name «New Population»(alias).
SELECT country_name, population * 1.1 AS New_Population
FROM countries;

-- 14. Remove all rows from countries table which has less than 100k population.
DELETE FROM countries
WHERE population < 100000;

-- 15. Remove all rows from countries_new table if country_id exists in countries table. Statement should return all deleted data.
SELECT * FROM countries_new
WHERE country_id IN (SELECT country_id FROM countries);

DELETE FROM countries_new
WHERE country_id IN (SELECT country_id FROM countries);
RETURNING *;

-- 16. Remove all rows from countries table. Statement should return all deleted data.
SELECT * FROM countries;

DELETE FROM countries;