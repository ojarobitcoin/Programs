#!/usr/bin/env python3
import os
#Password streght
special="~`!@#$%^&*()_-+={[}]|\:;<,>.?/"
u_count,l_count,s_count,n_count,total=0,0,0,0,0
#Text before program
print("""
This is a password streght testing software!
Minimum values for a valid password:
    Have at least one Upper_case
    Have at least one Number
    Have at least one special digit (  ~`!@#$%^&*()_-+={[}]|\:;<,>.?/  )
""")
#Os identification system
from sys import platform
if platform == "linux" or platform == "linux2":
    clear="clear"
elif platform == "darwin":
    clear="clear"
elif platform == "win32":
    clear="cls"
#Program start
pswrd=input("What's your password?")
os.system(clear)
print("\n"*13)
if len(pswrd) >= 8: 
    for i in pswrd:
        if i.isupper():
            u_count+=1
        if i.isdigit():
            n_count+=2
        if i in special:
            s_count+=3
        if i not in special and not i.isupper() and not i.isdigit() and not i.islower():
            print("ERROR YOUR PASSWORD CONTAINS A ILLEGAL CHARACTER!")
            quit()
else:
    print("The password has less than 8 characters.")
    quit()
#CHECK IF THE PASSWORD IS ATLEAST USABLE:
#It has to have at least one number, one special digit and an upper case letter.
if u_count==0:
    print("U don't have any Upper-Case letters, u should add some!")
    quit()
if n_count==0:
    print("U don't have any numbers, u should add some!")
    quit()
if s_count==0:
    print("U don't have any special characters, u should add some!")
    quit()
#CHECK THE STRENGHT OF THE PASSWORD
total=u_count+n_count+s_count+l_count
if total>=18:
    print("The password is REALLY REALLY STRONG\n(Your password is incredible, u should be proud of it!")
elif total>=14:
    print("The password is REALLY STRONG\n(To improve it increase the amount of numbers or characters or special digits!)")
elif total>=12:
    print("The password is STRONG\n(To improve it increase the amount of numbers or characters or special digits!)")
elif total>=10:
    print("The password is MEDIUM.\nU should improve it by increasing the amount of numbers or characters or special digits!)")
elif total>=6:
    print("The password is WEAK.\nIf you use this password it has a low security index.\nU should improve it by increasing the amount of numbers or characters or special digits!)")
print("\n\n")
