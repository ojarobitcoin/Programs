#Global variables
import mysql.connector
import os
mydb= mysql.connector.connect(
    host ="localhost",
    user= "guimbreon", 
    password= "password",
    database= "bank"    
)
my_cursor=mydb.cursor()
got=[]
def get(collum,table):
    my_cursor.execute(f"SELECT {collum} FROM {table};")
    for lines in my_cursor:
        got.append(lines[0])
table="people"
collum="money"
get(collum,table)
money=got
got=[]

table="earnings"
collum="perc"
get(collum,table)
perc=got
got=[]

table="earnings"
collum="returns"
get(collum,table)
returns=got
got=[]

#really starts here: makes the total
total=0
for value in money:
    total+=value 
each=[]
i=0
total_return=0
for value in returns:
    total_return+=int(((total*perc[i])/100)*value)/100
    i+=1
#count the lines in money(table) and:
#if it matches it'll update themine
#if it doesnt, it'll create or remove a l
my_cursor.execute("SELECT * FROM money;")
for lines in my_cursor:
    new=lines[2]
if new==int(total_return):
    print("The values haven't changed!")
else:
    my_cursor.execute(f"UPDATE money SET new={total_return} where id=1")
    mydb.commit()
    my_cursor.execute(f"UPDATE money SET old={new} where id=1")
    mydb.commit()