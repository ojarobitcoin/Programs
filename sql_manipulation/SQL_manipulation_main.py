#Global variables
import mysql.connector
import os
import pandas as pd
mydb= mysql.connector.connect(
    host ="localhost",
    user= "guimbreon", 
    password= "password",
    database= "bank"    
)
#takes money from people
my_cursor=mydb.cursor()
got=[]
def get():
    global collum, table
    my_cursor.execute(f"SELECT {collum} FROM {table};")
    for lines in my_cursor:
        got.append(lines[0])
table="people"
collum="money"
get()
money=got
got=[]

table="earnings"
collum="perc"
get()
perc=got
got=[]

table="earnings"
collum="returns"
get()
returns=got
got=[]

#really starts here: makes the total
total=0
for value in money:
    total+=value 
each=[]
i=0
for value in returns:
    each.append(int(((total*perc[i])/100)*value)/100)
    i+=1
total_return=0
for value in each:
    total_return+=value
    print(value)
print("\n",total_return)

#count the lines in money(table) and:
#if it matches it'll update themine
#if it doesnt, it'll create or remove a l
my_cursor.execute("SELECT * FROM money;")
for lines in my_cursor:
    old=lines[2]
print(old)
my_cursor.execute(f"UPDATE money SET new={total_return} where id=1")
mydb.commit()
my_cursor.execute(f"UPDATE money SET old={old} where id=1")
mydb.commit()