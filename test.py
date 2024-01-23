from mysqldb import *

rows = dbget("select * from emp")
for row in rows:
    print(row)
