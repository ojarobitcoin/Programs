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
print(mydb)
my_cursor=mydb.cursor()
i=1
while i<27:
    print(i)
    x=random.randint(0,10000)
    print(random.randint(0,10000))
    my_cursor.execute(f"INSERT INTO people VALUES({i},{x})")
    mydb.commit()
    i+=1