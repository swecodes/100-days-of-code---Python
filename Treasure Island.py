print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88   
''')

print("Welcome to Treasure Island. Your mission is to find the treasure")
choice1 = input("Left or Right ").lower()


if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake"
                      "Type 'wait' to wait for a boat. "
                      "Type 'swim' to swim across ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors."
                           "Yellow, Red and Blue. Which one do you choose? ").lower()
        if choice3 == "red":
            print("burned by fire game over.")
        elif choice3 == "blue":
            print("eaten by beasts. Game Over")
        elif choice3 == "yellow":
            print("you win")
        else:
            print("You chose a door that does not exist. Game Over!!")
    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")