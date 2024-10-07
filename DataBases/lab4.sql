
-- 1. Create database called «lab4»
CREATE DATABASE lab4;

-- 2. Create following tables «Warehouses» and «Boxes»:
create table if not exist Warehouses (
    code int serial primary key,
    location VARCHAR(255),
    capacity int
);

create table if not exist Boxes(
    code char(4) primary key,
    contents VARCHAR(255),
    value real,
    warehouse int
    --FOREIGN KEY (warehouse) REFERENCES Warehouses(code)
);

-- 4. Select all warehouses with all columns.
select * from warehouses;

-- 5. Select all boxes with a value larger than $150.
select * from boxes
where value > 150;

-- 6. Select all the boxes distinct by contents.
select distinct contents from boxes

-- 7. Select the warehouse code and the number of the boxes in each warehouse.
select warehouse, count(*) as box_count from Boxes
group by warehouse;

-- 8. Same as previous exercise, but select only those warehouses where the number of the boxes is greater than 2.
select warehouse, count(*) as box_count from Boxes
group by warehouse
having count(*) > 2;

-- 9. Create a new warehouse in New York with a capacity for 3 boxes.
insert into Warehouses(location, capacity)
values('New York', 3);

-- 10. Create a new box, with code "H5RT", containing "Papers" with a value of $200, and located in warehouse 2.
insert into Boxes (code, contents, value, warehouse)
values('H5RT', 'Papers', 200, 2);

-- 11. Reduce the value of the third largest box by 15%.
update Boxes
set value = value * 0.85
where code in (
    select code from Boxes
    order by value desc
    limit 1 offset 2
);

-- 12. Remove all boxes with a value lower than $150.
delete from boxes
where value < 150;

-- 13. Remove all boxes which is located in New York. Statement should return all deleted data.
delete from Boxes
using Warehouses
where Boxes.warehouse = Warehouses.code and Warehouses.location = 'New York'
returning *;



DROP TABLE IF EXISTS Warehouses;
DROP TABLE IF EXISTS Boxes;

\c postgres
DROP DATABASE IF EXISTS lab4;