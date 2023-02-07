# База Данных
# SQL язык базы данных
# СУВД - система управления базами данных
# crud create read update delete
import sqlite3

db = sqlite3.connect('test.db')

c = db.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS user(
name text,
title text,
view integer,
nick text
)
""");
#create
c.execute("INSERT INTO user VALUES('Samat', 'NOT', '10', 'Samat')")
#update
c.execute("SELECT rowid,* FROM user") # read
c.execute("UPDATE user SET name = 'Dasha' WHERE rowid = 1")
c.execute("UPDATE user SET name = 'Dasha' WHERE name = 'Samat'")
c.execute("UPDATE user SET name = 'x' WHERE rowid > 3")
c.execute("UPDATE user SET  view = 11 WHERE view = 10")
c.execute("UPDATE user SET  nick  = 'Dasha' WHERE rowid = 2")
c.execute("")
#delete
c.execute("DELETE FROM user WHERE rowid != ")

item = c.fetchall()
for el in item:
    print(el)

db.commit()
db.close()
