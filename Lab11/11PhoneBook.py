import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname="Lab11",
    user="postgres",
    password="postgres",
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute SQL commands
cur.execute("""
-- Procedure to insert new user by username and phone, update phone if user already exists
create or replace procedure insert_update(
    new_username varchar(255),
    new_phone varchar(255)
)
as $$
begin
    IF EXISTS(SELECT id FROM phonebook WHERE username = new_username) THEN
    UPDATE phonebook SET phone = new_phone WHERE username = new_username;
    ELSE
    INSERT INTO phonebook(username, phone)
    VALUES(new_username, new_phone);
    END IF;

end;
$$
language plpgsql;

-- Function that returns all records based on a pattern: prefix of phone number
create or replace function get_by_phone_prefix(pr varchar)
returns TABLE(username varchar(255), phone varchar(255)) as
$$
begin
    return query
    select phonebook.username, phonebook.phone from phonebook 
	where phonebook.phone like concat(pr, '%');
end;
$$
language plpgsql;


-- Procedure to insert many new users by list of username and phone. Use loop and if statement in stored procedure.  Check correctness of phone in procedure
create or replace procedure insert_many(
    new_username varchar(255)[],
    new_phone varchar(255)[]
)
as $$
begin
    FOR i IN 1..array_length(new_username, 1) LOOP
	IF LENGTH(new_phone[i]) < 12 THEN 
		INSERT INTO phonebook(username, phone) VALUES(new_username[i], new_phone[i]);
	END IF;
	END LOOP;
end;
$$
language plpgsql;

-- Function to query data from the phonebook table with pagination using limit and offset
create or replace function get_users_paginated(
    limit_val int,
    offset_val int
)
returns TABLE(username varchar(255), phone varchar(255)) as $$
begin
    return query
    select phonebook.username, phonebook.phone from phonebook 
    order by phonebook.username
    limit limit_val offset offset_val;
end;
$$
language plpgsql;

-- Procedure to delete data from the phonebook table by username or phone
create or replace procedure remove_user(
    del_username varchar(255),
    del_phone varchar(255)
)
as $$
begin
    DELETE FROM phonebook WHERE username = del_username OR phone = del_phone;
end;
$$
language plpgsql;
""")
conn.commit()



# Close the cursor
cur.close()

# Open a new cursor
cur = conn.cursor()

def main():
    # Test insert_update procedure
    print("Testing insert_update procedure...")
    cur.execute("CALL insert_update('John Doe', '1234567890')")
    conn.commit()

    # Test get_by_phone_prefix function
    print("Testing get_by_phone_prefix function...")
    cur.execute("SELECT * FROM get_by_phone_prefix('123')")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Test insert_many procedure
    print("Testing insert_many procedure...")
    cur.execute("CALL insert_many(ARRAY['Alice', 'Bob'], ARRAY['2345678901', '3456789012'])")
    conn.commit()

    # Test get_users_paginated function
    print("Testing get_users_paginated function...")
    cur.execute("SELECT * FROM get_users_paginated(10, 0)")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Test delete_user procedure
    print("Testing delete_user procedure...")
    cur.execute("CALL remove_user('John Doe', '1234567890')")
    conn.commit()

    cur.close()

main()

