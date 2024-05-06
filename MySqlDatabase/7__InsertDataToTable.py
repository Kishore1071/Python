import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="test_db"
)

mysql_cursor = mysql_db.cursor()

query = "insert into customers (name, address) values (%s, %s)"


# For Single Record

# values = ("Kishore", "Cheyur", 25)

# mysql_cursor.execute(query, values)

# For Multiple Record

values = [
    ("Kishore", "Cheyur"),
    ("Stark", "New York")
]

mysql_cursor.executemany(query, values)

mysql_db.commit()

print(mysql_cursor.rowcount, "New Record Added")

print(mysql_cursor.lastrowid, "Id Of New Record Added")