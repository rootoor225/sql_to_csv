##### CODE DOESN'T WORK ? #####

# code: ascii

import MySQLdb as dbapi
import sys
import csv

# Be sure the SQLCommand stored in the variable QUERY is ended by a semi-colon ";"
# Add the database name to the db variable or Command
# use "w" as file writing format option
# if you still want to use "wb"  go to the python files managing course  for more details about binary format


QUERY='SELECT * FROM table_name;'
db=dbapi.connect(host='localhost',user='root',passwd='password',db='your-mysql-db-name')

cur=db.cursor()
cur.execute(QUERY)
result=cur.fetchall()

c = csv.writer(open("dbdump01.csv", "w"))
for x in result:
    c.writerow(x)
