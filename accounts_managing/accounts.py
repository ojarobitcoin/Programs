import mysql.connector
from getpass import getpass
mydb= mysql.connector.connect(
    host ="localhost",
    user= "user", 
    password= "password",
    database= "accounts"    
)
my_cursor=mydb.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS people (name varchar(255), email varchar(255), password varchar(255));")
mydb.commit()
name=input("What's your name?\n>>")
password=getpass("What's your password?\n>>")
my_cursor.execute("SELECT email FROM people;")
all_emails,mail_extensions=[],["@gmail.com","@gmail.pt","outlook.pt","outlook.com","hotmail.pt","hotmail.com"]
for item in my_cursor:
    all_emails.append(item[0])
email=input("What's your email?\n>>")

aproved=0
while aproved!=2:
    if email in all_emails:
        aproved=0
        email=input("ERROR:email already exists\n\nWhat's your email?\n>>")
    if email not in all_emails:
        aproved+=1
    if "@" not in email:
        aproved=0
        email=input("ERROR:email has to have @\n\nWhat's your email?\n>>")
    elif "@" in email:
            aproved+=1

my_cursor.execute(f"INSERT INTO people VALUES('{name}','{email}','{password}');")
mydb.commit()