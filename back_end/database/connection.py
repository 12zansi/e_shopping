import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "e_shopping",
    port = 3366
  )

cursor = connection.cursor()