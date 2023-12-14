import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="test_db"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("create table customers (id int auto_increment primary key , name varchar(255), address varchar(255))")















