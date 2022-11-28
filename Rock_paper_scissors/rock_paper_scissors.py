#!/usr/bin/env python3
#Rock, paper and scissors
import random
import os
#Global variables
points,points_bot,i=0,0,0
all_you=["0",]*3
all_bot=["0",]*3
#Os identification system
from sys import platform
if platform == "linux" or platform == "linux2":
    clear="clear"
elif platform == "darwin":
    clear="clear"
elif platform == "win32":
    clear="cls"
#Program start
def whole():
    global points_bot, points, all_you,all_bot #points out the global variables to use it
    choices=["rock","paper","scissors"]
    your_choice=input("What's your choice?\nrock\npaper\nscissors\n=")
    all_you[i]=your_choice
    if your_choice not in choices:
        print("Your input was incorrect, try again!\n")
        quit()
    #Machine choice
    machine_choice=random.choice(choices)
    all_bot[i]=machine_choice
    print(f"\n\n\nThe machine choice was {machine_choice} and yours was {your_choice}.")
    #your_choice is paper
    if your_choice=="paper" and machine_choice=="rock":
        print("u won\n")
        points+=1
    elif your_choice=="paper" and machine_choice=="scissors":
        print("u lost\n")
        points_bot+=1
    elif your_choice==machine_choice: #This goes for every choice in this game
        print("it was a draw\n") #it was a draw which means no-one gets points
    #your_choice is rock
    if your_choice=="rock" and machine_choice=="paper":
        print("u lost\n")
        points_bot+=1
    elif your_choice=="rock" and machine_choice=="scissors":
        print("u won\n")
        points+=1
    #your_choice is scissors
    if your_choice=="scissors" and machine_choice=="rock":
        print("u lost\n")
        points_bot+=1
    elif your_choice=="scissors" and machine_choice=="paper":
        print("u won\n")
        points+=1
def final():
    print("The log of the game:\n")
    print(f"U choosed {all_you[0]} and the bot choosed {all_bot[0]} on the first game.")
    print(f"U choosed {all_you[1]} and the bot choosed {all_bot[1]} on the second game.")
    print(f"U choosed {all_you[2]} and the bot choosed {all_bot[2]} on the third game.\n\n")
print("""Here is the rock paper scissors game:
The rules are:
-It's a best of 3 game.
-The rock wins against scissors and loses against paper
-The scissors wins agains paper and loses against rock
-The paper wins against rock and loses against scissors""")
input("\nPress enter to continue...")
os.system(clear)
while i < 3:
    choices=["rock","paper","scissors"]
    whole()
    i+=1   
    input("\nPress enter to continue...")
    os.system(clear)  #clears all of the code above(just to make it look cleaner)
    print(f"U have {points} and the bot has {points_bot}")
input("\nPress enter to continue...")
if points>points_bot:
    print("\n\n\n\n\n")
    final()
    print("U won the best of 3 game of Rock, paper and scissors.\n")
elif points<points_bot:
    print("\n\n\n\n\n")
    final()
    print("U lost the best of 3 game of Rock, paper and scissors.\n")
else:
    print("\n\n\n\n\n")
    final()
    print('\033[1m'+"The best of 3 game of Rock, paper and scissors was a draw.\n"+'\033[1m' )
