import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user= "abc",
    password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mycursor.execute("insert into test1.test_table values(5285,'sudh',4663,546.52,'namit')")
mydb.commit()
mydb.close()