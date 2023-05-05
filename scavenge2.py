import csv
import sqlite3
import random

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect("scavenge2.db")

# Open a cursor to perform database operations
c = conn.cursor()

# Clear the "items" table (if it exists)
c.execute("DROP TABLE IF EXISTS items")

# Create the "items" table with columns from the CSV file
with open("scavenge2.csv", "r", newline="") as f:
    reader = csv.reader(f)
    headers = next(reader)
    query = "CREATE TABLE items ({})".format(", ".join(headers))
    c.execute(query)

# Import data from the CSV file into the "items" table
with open("scavenge2.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        query = "INSERT INTO items ({}) VALUES ({})".format(
            ", ".join(row.keys()), ", ".join(["?"] * len(row))
        )
        c.execute(query, list(row.values()))

# Commit the changes
conn.commit()

# Ask the user how many items to roll for
num_items = int(input("How many items would you like to roll for? "))

# Select and print random items from the database
print("You found:")
for i in range(num_items):
    c.execute("SELECT Item, Size, Level FROM items ORDER BY RANDOM() LIMIT 1")
    item = c.fetchone()
    print("{} ({}, {})".format(item[0], item[1], item[2]))

# Close the cursor and the database connection
c.close()
conn.close()
