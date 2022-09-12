import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="e_shopping",
  port=3366
)

my_cursor = my_db.cursor()