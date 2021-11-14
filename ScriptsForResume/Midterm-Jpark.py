#!/usr/bin/env python3

print("\n")
print("Name: Aaron Liebgold")
print("\n")

password_database = {
    'UserName':'dnedry',
    'Password':'Please'
}

command_database = {
    'Reboot':'Ok. I will reboot all park systems.',
    'Shutdown':'Ok. I will shutdown all park systems.',
    'Done':'I hate all this hacker stuff'
}


white_rabbit_object='0'
counter='0'

MagicWord=("You Didnt Say The Magic Word, please try again.")

while password_database:
    SignIn = input("Username: ")
    if SignIn == "dnedry":

        password = input("Password: ")
        if password == "please":
            print("Hello Dennis,You are still the best hacker in Jusrasic Park")

            break
        if SignIn != "dnedry":
            print(MagicWord * 25)

        if password != "please":
            print(MagicWord * 25)




while command_database:
        choices = input("Please enter a Command {Reboot,Shutdown,Done}:")
        if choices == "Reboot":
            print(command_database['Reboot'])
        if choices == "Shutdown":
            print(command_database['Shutdown'])
        if choices == "Done":
            print(command_database['Done'])
        else:
            print("The Lysin Contingency Has Gone into effect")
