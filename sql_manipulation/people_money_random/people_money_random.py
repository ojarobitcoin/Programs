#Global variables
#CREATE TABLE people (id int, money int) ->creates a  new table
#DROP TABLE people ->destroy table
import mysql.connector
import random
mydb= mysql.connector.connect(
    host ="localhost",
    user= "guimbreon", 
    password= "password",
    database= "bank"    
)
my_cursor=mydb.cursor()
#Add stuff to the table people
i,id=0,0
my_cursor.execute(f"SELECT id FROM people;")
for lines in my_cursor:
    i+=1
while id<10:
    id+=1
    i+=1
    money=random.randint(0,10000)
    my_cursor.execute(f"INSERT INTO people VALUES({i},{money})")
    mydb.commit()
#Add stuff to the table earnings
i,id,total=0,0,100
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