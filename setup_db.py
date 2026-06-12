import sqlite3

# 1. Connect to the database (this automatically creates a file called 'customers.db')
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

# 2. Write SQL to create a Table (like creating a spreadsheet with columns)
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount_due INTEGER,
    status TEXT
)
''')

# 3. Clear any old data so we start fresh
cursor.execute('DELETE FROM customers')

# 4. Our raw data
mock_data = [
    ("Aisha", 4500, "overdue"),
    ("Rahul", 0, "paid"),
    ("Priya", 1200, "overdue"),
    ("Vikram", 0, "paid"),
    ("Neha", 8500, "overdue")
]

# 5. Write SQL to insert the data into our table
cursor.executemany('''
INSERT INTO customers (name, amount_due, status)
VALUES (?, ?, ?)
''', mock_data)

# 6. Save the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete! Look in your VS Code folder for 'customers.db'.")