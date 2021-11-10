#!/usr/bin/env python3
###########################################
#  Practicing Flow controll using         #
#  a story line and elif, if statements   #
#  there is one else statement at the end #
###########################################

print("You enter a mystery room with 3 doors.\nDo you go through Door #1 or Door #2 or Door#3")

Door=input(">")

if Door == "1":
    print("\nThere is a guy with a sword  about to chop your head off.")
    print("What do you do?")
    print("1. Turn around and run!")
    print("2. Go ahead kill me know!")

    killer=input(">")
    if killer =="1":
        print("You are now being chased by a killer!")
    if killer == "2":
        print("Congratulations, you are now dead!") 

elif Door == "2":
    print("There is a bag with $100,000 staring right at you!")
    print("what do you do?")
    print("1. Take the money and run!")
    print("2. Return the money to the police for a $500 reward!")

    money = input(">")
    if money =="1":
        print("You are now $100,000 richer!")
    if money =="2":
        print("You are now $500 richer!")

elif Door == "3":
    print("You now get to choose RICH? or HAPPY?")
    print("What do you choose?")
    print("1. Rich")
    print("2. Happy")

    choose = input(">")
    if choose =="1":
        print("Congratulations, You are now rich but will never be happy!")
    elif choose =="2":
        print("Good for you! Rich is just another name for Dick.")

    else:
        print("Are you that indecisive and unable to choose?")
