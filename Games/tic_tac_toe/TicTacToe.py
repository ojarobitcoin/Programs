import random
input("""
Welcome to TIK TAK TOE!
After playing u'll be asked which simbol each player wants to play has...

The model of the game is the follwoing:
1|2|3
4|5|6
7|8|9

U'll have to say the number corresponding to the spot u want to play in.

Press any key to continue...""")
key=[""]*3
key[1]=input("PLAYER 1:\nWhich simbol do you u want to play has?\n>>")
key[2]=input("PLAYER 2:\nWhich simbol do you u want to play has?\n>>")
which=random.randint(1,2)
print(f"The machine will choose who plays first randomly!\nThe PLAYER {which} plays first!")
end=0
def check(i):
    global which,end
    if play[1]==play[2] and play[2]==play[3]:
        end=1
    elif play[4]==play[5] and play[5]==play[6]:
        end=1
    elif play[7]==play[8] and play[8]==play[9]:
        end=1
    elif play[1]==play[4] and play[4]==play[7]:
        end=1
    elif play[2]==play[5] and play[5]==play[8]:
        end=1
    elif play[3]==play[6] and play[6]==play[9]:
        end=1
    elif play[1]==play[5] and play[5]==play[9]:
        end=1
    elif play[3]==play[5] and play[5]==play[7]:
        end=1
    
    if which==1 and end==0:
        which+=1
    elif which==2 and end==0:
        which-=1
play=[0,1,2,3,4,5,6,7,8,9]
for thing in play:
    if end==1:
        continue
    i=int(input(f"""Where do you wanna play PLAYER {which}?\n
                {play[1]}|{play[2]}|{play[3]}
                {play[4]}|{play[5]}|{play[6]}
                {play[7]}|{play[8]}|{play[9]}
    >>"""))
    if play[i]==key[1] or play[i]==key[2]:
        input("U can't choose that spot!")
    play[i]=key[which]
    check(i)
print(f"""
FINAL!
                1|2|3\t\t{play[1]}|{play[2]}|{play[3]}
                4|5|6\t\t{play[4]}|{play[5]}|{play[6]}
                7|8|9\t\t{play[7]}|{play[8]}|{play[9]}
PLAYER {which} u won!
    """)