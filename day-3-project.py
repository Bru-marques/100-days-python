# Treasure game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


answer1 = str.lower(input("Which is you choise = Left or Right?\n"))
if answer1 == "left":
    answer2 = str.lower(input("What are you do = Swim or wait?\n"))
    if answer2 == "wait":
        answer3 = str.lower(
            input("Which door do you prefer = Red, Blue or Yellow?\n"))
        if answer3 == "yellow":
            print("*** YOU WIN ***")
        elif answer3 == "blue":
            print("Oh no, you were ate by a beast.\n  »»»GAME OVER«««")
        elif answer3 == "red":
            print("You are burned by fire. \n  »»»GAME OVER«««")
    else:
        print("Oh no, you were attacked by a trout.\n  »»»GAME OVER«««")
else:
    print("You fall into a hole \n  »»»GAME OVER«««")