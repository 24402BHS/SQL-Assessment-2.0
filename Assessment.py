import sqlite3

DATABASE = "Music.db"

db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM albums;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close