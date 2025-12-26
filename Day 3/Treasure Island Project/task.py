print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
#GAMEPLAYER'S INPUTS AND OUTCOMES
choice1 = input("You've reached a fork in the path\nChoose a direction:\n"
                "1. Go left\n2. Go right\nEnter 1 or 2: ")
if choice1 == "1":
    action = input("A river blocks your path.\nWhat will you do?\n"
                   "1. Swim across\n"
                   "2. Wait for help\n"
                   "Enter 1 or 2: ")
    if action == "2":
        door = input("You find three doors.\nEach door has a different color.\nChoose wisely:\n"
    "1. Red door\n"
    "2. Blue door\n"
    "3. Yellow door\n"
    "Enter 1, 2, or 3: ")
        if door == "1":
            print("Burned by Fire.\n GAME OVER!")
        elif door == "2":
            print("Eaten by beasts.\n GAME OVER!")
        elif door == "3":
            print("Congratulations!\nYOU HAVE FOUND THE TREASURE!")
            exit()
        else:
            print("GAME OVER!")
    else:
        print("Attacked by the trout.\nGAME OVER")
else:
    print("You fell into a hole.\nGAME OVER!")


