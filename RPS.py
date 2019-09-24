player = input("Enter r,p,s: ")

from random import *
x = randint(1, 3)

if player == ("r"):
    print ("you picked rock")
    if (x) == (1):
        print ("Tie")
    elif (x) == (2):
        print ("You Lose")
    elif (x) == (3):
        print ("You Win!")

elif player == ("p"):
    print ("you picked paper")
    if (x) == (1):
        print ("You Win!")
    elif (x) == (2):
        print ("Tie")
    elif (x) == (3):
        print ("You Lose")

elif player == ("s"):
    print ("you picked scissors")
    if (x) == (1):
        print ("You Lose")
    elif (x) == (2):
        print ("You Win!")
    elif (x) == (3):
        print ("Tie")
else:
    print ("please try again")

input('Press ENTER to exit')
