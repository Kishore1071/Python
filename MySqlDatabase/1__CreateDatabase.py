import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("create database test_db")