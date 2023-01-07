import mysql.connector
from getpass import getpass
mydb= mysql.connector.connect(
    host ="localhost",
    user= "guimbreon", 
    password= "password",
    database= "accounts"    
)
my_cursor=mydb.cursor()
my_cursor.execute("CREATE TABLE IF NOT EXISTS people (name varchar(255), email varchar(255), password varchar(255));")

all_emails,all_passwords,mail_extensions=[],[],["@gmail.com","@gmail.pt","outlook.pt","outlook.com","hotmail.pt","hotmail.com"]#after: make this a thing

choice=int(input("What do you want to for?\n1-Login\n2-Register\n>>"))
if choice==1:
    email=input("What's your email?\n>>")
    aproved=0
    while aproved!=2:
        my_cursor.execute("SELECT email FROM people;")
        for item in my_cursor:
            all_emails.append(item[0])
        while aproved!=2:
            if email not in all_emails:
                aproved=0
                email=input("ERROR:email doesn't exists\n\n\n>>")
            if email in all_emails:
                aproved+=1
            if "@" not in email and aproved==1:
                aproved=0
                email=input("ERROR:email has to have @\n\nWhat's your email?\n>>")
            elif "@" in email and aproved==1:
                    aproved+=1
        i=0
        print(i)
        password=input("What't your password?")
        my_cursor.execute("SELECT emailFROM people;")
        for item in my_cursor:
            all_passwords.append(item[0])
        
        for item in all_emails:
            if email==all_emails:
                i=i
            else:
                i+=1
        if password==all_passwords[i]:
            print("U ENTERED YOUR ACCOUNT")
        

if choice==2:
    #REGISTER
    mydb.commit()
    name=input("What's your name?\n>>")
    password=getpass("What's your password?\n>>")
    my_cursor.execute("SELECT email FROM people;")
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