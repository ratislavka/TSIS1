import csv
import psycopg2

def create_table(cur):
    cur.execute("""
        CREATE TABLE PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(15)
        )
    """)

def insert_from_csv(cur, filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                row
            )

def insert_from_console(cur):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")

    cur.execute(
        "INSERT INTO PhoneBook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )

def update_data(cur):
    new_first_name = input("Enter new first name: ")
    phone = input("Enter phone number to update: ")

    cur.execute(
        "UPDATE PhoneBook SET first_name = %s WHERE phone = %s",
        (new_first_name, phone)
    )

def query_data(cur):
    filter_value = input("Enter filter value: ")

    cur.execute(
        "SELECT * FROM PhoneBook WHERE first_name LIKE %s",
        (f"%{filter_value}%",)
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

def delete_data(cur):
    phone = input("Enter phone number to delete: ")

    cur.execute(
        "DELETE FROM PhoneBook WHERE phone = %s",
        (phone,)
    )

def main():
    conn = psycopg2.connect("dbname= user= password=")
    cur = conn.cursor()

    create_table(cur)
    insert_from_csv(cur, 'phonebook.csv')
    insert_from_console(cur)
    update_data(cur)
    query_data(cur)
    delete_data(cur)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
