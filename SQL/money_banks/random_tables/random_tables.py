#CREATE DATABASE bank;
import mysql.connector
import random
mydb= mysql.connector.connect(
    host ="localhost",
    user= "user", 
    password= "password",
    database= "bank"    
)
my_cursor=mydb.cursor()
#Add stuff to the table people
i,id=0,0
my_cursor.execute("DROP TABLE IF EXISTS people;")
my_cursor.execute("CREATE TABLE IF NOT EXISTS people (id int, money int);")
#my_cursor.execute(f"SELECT id FROM people;")  #ADD this thing if u want to delete line 13 and only create new items in the table
#for lines in my_cursor:   
#    i+=1
while id<26:
    id+=1
    i+=1
    money=random.randint(0,10000)
    my_cursor.execute(f"INSERT INTO people VALUES({i},{money})")
    mydb.commit()
#Add stuff to the table earnings
i,id,total=0,0,100
my_cursor.execute("DROP TABLE IF EXISTS earnings;")
my_cursor.execute("CREATE TABLE IF NOT EXISTS earnings(id int, perc float, returns float);")
my_cursor.execute(f"SELECT * FROM earnings;")
for lines in my_cursor:
    i+=1
while total>0:
    id+=1
    i+=1
    returns=random.uniform(0,13)
    perc=random.uniform(2,15)
    my_cursor.execute(f"INSERT INTO earnings VALUES({i},{perc},{returns})")
    mydb.commit()
    total-=perc
    print
    if total==0:
        break
    else:
        continue
#Create if does't exit the money table
i=0
my_cursor.execute("CREATE TABLE IF NOT EXISTS money(id int, old float, new float);")
my_cursor.execute(f"SELECT id FROM money")
for lines in my_cursor:   
    i+=1
if i==0:
    my_cursor.execute("INSERT INTO money VALUES (1,0,0);")
    mydb.commit()