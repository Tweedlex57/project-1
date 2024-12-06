import sqlite3
con = sqlite3.connect('coffee.sqlite')

cur = con.cursor()

result = cur.execute("""SELECT * FROM coffe""").fetchall()

for i in result:
    print(i)

con.close()