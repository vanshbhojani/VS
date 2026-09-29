import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vansh#2004",
    # database="dc_",
    port=3306
)

print("Connected successfully!")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS dc_")

cursor.execute("USE dc_")

# Create a table
cursor.execute(
    """
    create table if not exists employee(
        id int primary key auto_increment,
        name varchar(255),
        age int,
        address varchar(255),
        salary float

    )
"""
)
cursor.execute("""
    INSERT INTO employee (name, age, address, salary)
    VALUES
        ("John Doe", 30, "123 Main St", 50000.50),
        ("Jane Doe", 25, "456 Elm St", 60000.75),
        ("Bob Smith", 40, "789 Oak St", 70000.00),
        ("Alice Johnson", 35, "987 Pine St", 80000.25),
        ("Charlie Brown", 28, "678 Maple St", 90000.00),
        ("David Williams", 22, "901 Willow St", 95000.50),
        ("Eve Jones", 28, "654 Cedar St", 100000.75),
        ("Frank Lee", 22, "321 Oak St", 110000.00)
""")

conn.commit()
conn.close()