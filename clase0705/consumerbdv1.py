import sqlite3

conectionCx=sqlite3.connect('basev1.db')

co=conectionCx.cursor()
sqlSx="select * from users"

data=co.execute(sqlSx).fetchall()

print(type(data))

for i in data:
    print(i[0],i[1],i[2],i[3])
