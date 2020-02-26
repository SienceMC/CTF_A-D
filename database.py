import sqlite3

conn = sqlite3.connect('ctf.db')

cur = conn.cursor()


# Create Database flags
# cur.execute("""CREATE TABLE flags (
#      flag BLOB,
#      points INTEGER
#      )""")

# Create Database teams
# cur.execute("""CREATE TABLE teams (
#     name TEXT,
#     points INTEGER
#     )""")



# Insert into Database
# cur.execute("INSERT INTO teams VALUES ('Team 1', 5000)")
# conn.commit()

# Delete from Database
# cur.execute("""DELETE FROM teams""")
# conn.commit


# Fetch from Database
cur.execute("SELECT * FROM teams")
print(cur.fetchall())

conn.close()


