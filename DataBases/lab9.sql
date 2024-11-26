-- 1. Write a stored procedure named increase_value that takes one integer parameter and returns the parameter value increased by 10.
CREATE FUNCTION increase_value(par int)
RETURNS int AS $$
BEGIN
    RETURN par + 10;
END;
$$ LANGUAGE plpgsql;

SELECT increase_value(5);



-- 2. Create a stored procedure compare_numbers that takes two integers and returns 'Greater', 'Equal', or ‘Lesser' as an out parameter,
-- depending on the comparison result of these two numbers.
CREATE FUNCTION compare_numbers(a int, b int)
RETURNS varchar AS $$
BEGIN
    IF a > b THEN
        RETURN 'Greater';
    ELSIF a < b THEN
        RETURN 'Less';
    ELSE
        RETURN 'Equal';
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT compare_numbers(5, 6);


-- 3. Write a stored procedure number_series that takes an integer n and returns a series from 1 to n. Use a looping construct within the procedure.
CREATE FUNCTION number_series(n int)
RETURNS TABLE(num int) AS $$
BEGIN
    FOR num IN 1..n LOOP
        RETURN NEXT num;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM number_series(5);


-- 4. Write a stored procedure find_employee that takes an employee name as a parameter and returns the employee details by performing a query.
CREATE FUNCTION find_employee(emp_name varchar)
RETURNS TABLE(employee_id int, employee_name varchar, department varchar, salary numeric) AS $$
BEGIN
    RETURN QUERY
    SELECT e.employee_id, e.employee_name, e.department, e.salary FROM employees e
    WHERE e.employee_name = emp_name;
END;
$$ LANGUAGE plpgsql;

-- Example usage
SELECT * FROM find_employee('Johny Depp');


-- 5. Develop a stored procedure list_products that returns a table with product details from a given category.
CREATE FUNCTION list_products(category varchar)
RETURNS TABLE(product_name varchar, price numeric) AS $$
BEGIN
    RETURN QUERY
    SELECT p.product_name, p.price FROM products p
    WHERE p.category = category;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM list_products('Electronics');


-- 6. Create two stored procedures where the first procedure calls the second one. For example, a procedure calculate_bonus
-- that calculates a bonus, and another procedure update_salary that uses calculate_bonus to update the salary of an employee.
CREATE FUNCTION add_bonus(bonus numeric(10, 2), emp_name VARCHAR)
RETURNS void
AS $$
BEGIN
    UPDATE employees
    SET salary = salary + bonus
    WHERE employee_name = emp_name;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION calculate_bonus(emp_name varchar, overtime_hours int)
RETURNS numeric AS $$
DECLARE
    emp_salary numeric;
    bonus numeric;
BEGIN
    SELECT salary INTO emp_salary FROM employees
    WHERE employee_name = emp_name;

    bonus := (emp_salary / 1200) * 0.2 * overtime_hours;

    PERFORM add_bonus(bonus, emp_name);

    RETURN bonus;
END;
$$ LANGUAGE plpgsql;

SELECT calculate_bonus('Brad Pitt', 10);


-- 7.
CREATE OR REPLACE FUNCTION complex_calculation(emp_name VARCHAR, salary NUMERIC, percent_increase NUMERIC)
RETURNS VARCHAR AS $$
DECLARE
    new_salary NUMERIC;
    reversed_name VARCHAR;
    result_message VARCHAR;
BEGIN
    -- Label for the main block
    main_block: BEGIN
        -- First sub-block: Numeric computation
        numeric_block: BEGIN
            new_salary := salary + (salary * percent_increase / 100);
        END numeric_block;

        -- Second sub-block: String manipulation
        string_block: BEGIN
            reversed_name := reverse(emp_name);
        END string_block;

        -- Combine results from both sub-blocks
        result_message := 'Employee ' || reversed_name || ' now has a new salary: ' || round(new_salary, 2);
    END main_block;

    -- Return the final result
    RETURN result_message;
END;
$$ LANGUAGE plpgsql;


SELECT complex_calculation('Leonardo', 50000, 10);


