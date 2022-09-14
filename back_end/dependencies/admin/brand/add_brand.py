from database.connection import my_cursor,my_db


sql = "UPDATE brand SET name = 'addidas' WHERE id = '1'"

my_cursor.execute(sql)

my_db.commit()
