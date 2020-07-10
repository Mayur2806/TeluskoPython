
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'Mayur@28', database = 'Telusko')
# connection done
mycursor = mydb.cursor()
# cursor created
mycursor.execute('insert into student values(3, "Dev", "ETC")')
mycursor.execute('select * from student')
# Query fired
result = mycursor.fetchall()
# data stored in result
for i in result:
    print(i)
