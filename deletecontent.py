import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('DELETE FROM content WHERE id = 957')
conn.commit()
conn.close()