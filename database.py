import sqlite3

conn = sqlite3.connect('ctf.db')

cur = conn.cursor()

# cur.execute("""CREATE TABLE flags (
#      flag BLOB,
#      points INTEGER
#      )""")

# cur.execute("INSERT INTO flags VALUES ('FLAG{1234}', 100)")

cur.execute("SELECT * FROM flags")

print(cur.fetchall())


conn.commit()

conn.close()

# cur.execute("""CREATE TABLE teams (
    
    
    
#     )""")
