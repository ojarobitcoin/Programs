#!/usr/bin/python3
import mysql.connector
import os

mydb= mysql.connector.connect(
    host ="localhost",
    user= "your_user", 
    password= "password",
    database= "name"    
)
print(mydb)
my_cursor=mydb.cursor()
def get():
    global what, where
    my_cursor.execute(f"SELECT {what} FROM {where};")
    i=0
    for collumn in my_cursor:
        i+=1
    test=["",]*i
    i=0
    my_cursor.execute(f"SELECT {what} FROM {where};")
    for collumn in my_cursor:
        test[i]=collumn[0]
        i+=1
    print(test)
#tables
os.system("clear")
my_cursor.execute("SHOW TABLES;")
print("Here are the disponible tables:")
for tables in my_cursor:
    print(tables[0])
where=str(input("From which table?\n>>"))
#collumn
os.system("clear")
print(f"\nHere are the available collumns:")
my_cursor.execute(f"DESCRIBE {where};")
i=0
for collumn in my_cursor:
    print(collumn[0])
what=str(input("Which collumn do u want to get?\n>>"))
get()
