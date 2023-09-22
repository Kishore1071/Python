import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

# Adding New Column

mysql_cursor.execute("alter table customers add column age int")

# Delete Column

mysql_cursor.execute("alter table customers drop column age")

# Change Column Name

mysql_cursor.execute("alter table customers rename column age to customer_age")

# Change Column Datatype

mysql_cursor.execute("alter table customers modify column customer_age varchar(255)")