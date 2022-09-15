from database.connection import cursor,connection


sql = "UPDATE brand SET name = 'addidas' WHERE id = '1'"

cursor.execute(sql)

connection.commit()
