-- 1. Create database called «lab4»
CREATE DATABASE lab4;

-- 2. Create following tables «Warehouses» and «Boxes»:
CREATE TABLE IF NOT EXISTS warehouses (
    code SERIAL PRIMARY KEY,
    location VARCHAR(255),
    capacity INT
);

CREATE TABLE IF NOT EXISTS boxes (
    code VARCHAR(4) PRIMARY KEY,
    contents VARCHAR(255),
    value INT,
    warehouse INT
);

-- 3.
INSERT INTO warehouses(code, location, capacity) VALUES(1, 'Chicago', 3);
INSERT INTO warehouses(code, location, capacity) VALUES(2, 'Chicago', 4);
INSERT INTO warehouses(code, location, capacity) VALUES(3, 'New York', 7);
INSERT INTO warehouses(code, location, capacity) VALUES(4, 'Los Angeles', 2);
INSERT INTO warehouses(code, location, capacity) VALUES(5, 'San Francisco', 8);

INSERT INTO boxes(code, contents, value, warehouse) VALUES('0MN7', 'Rocks', 180, 3);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('4H8P', 'Rocks', 250, 1);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('4RT3', 'Scissors', 190, 4);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('7G3H', 'Rocks', 200, 1);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('8NJ6', 'Papers', 75, 1);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('8Y6U', 'Papers', 50, 3);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('9J6F', 'Papers', 175, 2);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('LL08', 'Rocks', 140, 4);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('P0H6', 'Scissors', 125, 1);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('P2T6', 'Scissors', 150, 2);
INSERT INTO boxes(code, contents, value, warehouse) VALUES('TU55', 'Rocks', 90, 5);

-- 4. Select all warehouses with all columns.
SELECT * FROM warehouses;

-- 5. Select all boxes with a value larger than $150.
SELECT * FROM boxes
WHERE value > 150;

-- 6. Select all the boxes distinct by contents.
SELECT DISTINCT contents FROM boxes;

-- 7. Select the warehouse code and the number of the boxes in each warehouse.
SELECT warehouse, COUNT(*) AS box_count FROM boxes
GROUP BY warehouse;

-- 8. Same as previous exercise, but select only those warehouses where the number of the boxes is greater than 2.
SELECT warehouse, COUNT(*) AS box_count FROM boxes
GROUP BY warehouse
HAVING COUNT(*) > 2;

-- 9. Create a new warehouse in New York with a capacity for 3 boxes.
INSERT INTO warehouses(location, capacity)
VALUES('New York', 3);

-- 10. Create a new box, with code "H5RT", containing "Papers" with a value of $200, and located in warehouse 2.
INSERT INTO boxes (code, contents, value, warehouse)
VALUES('H5RT', 'Papers', 200, 2);

-- 11. Reduce the value of the third largest box by 15%.
UPDATE boxes
SET value = value * 0.85
WHERE value = (
    SELECT value FROM boxes
    ORDER BY value DESC  -- the highest value will be first
    LIMIT 1  -- restricts the output to just one row.  (if no "limit 1": returns all values starting from the third largest)
    OFFSET 2 -- skips the first two rows of the sorted result
);

-- 12. Remove all boxes with a value lower than $150.
DELETE FROM boxes
WHERE value < 150;

-- 13. Remove all boxes which is located in New York. Statement should return all deleted data.
DELETE FROM boxes
WHERE warehouse IN (
    SELECT code FROM warehouses
    WHERE location = 'New York'
)
RETURNING *;

DROP TABLE IF EXISTS warehouses;
DROP TABLE IF EXISTS boxes;

\c postgres
DROP DATABASE IF EXISTS lab4;
