import sqlite3

db = sqlite3.connect("assessment.db")
conn = db.cursor()
sql = "SELECT Name, HP FROM Brawlers ORDER BY HP desc;"
conn.execute(sql)
result = conn.fetchall()
print(result)

db.close()
