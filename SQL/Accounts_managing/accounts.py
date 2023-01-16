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


all_items={}


#GET ALL INFO
my_cursor.execute("SELECT * FROM people;")
for item in my_cursor:
    all_items[item[1]]=item[2]

#MAIN PROGRAM
choice=int(input("What do you want to for?\n1-Login\n2-Register\n>>"))
if choice==1:
    aproved,tries=0,0
    while aproved!=1:
        if tries==0:
            email=input("What's your email?\n>>")
        else:
            email=input("ERROR:The inputed email doesn't exist in our database\n\nWhat's your email?\n>>")
        for name in all_items:
            if email==name:
                aproved=1
        tries+=1
    aproved,tries=0,0
    while aproved!=1:
        if tries==0:
            password=input("What's your password?\n>>")
        else:
            password=input("ERROR:WRONG PASSWORD!\n\nWhat's your email?\n>>")
        for name in all_items:
            if password==all_items[name]:
                aproved=1
        tries+=1
    print("U HAVE ENTERED YOUR ACCOUNT!")
elif choice==2:
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

else:
    print("The choice u made is not possible!")
