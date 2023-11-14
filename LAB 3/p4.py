# Q4 Write a Python program to connect to MySQL database.

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="laxmi103" 
)
print(mydb)