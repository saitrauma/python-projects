
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


direction = input("left or right?")
if direction == "left":
    option = input("do u wanna swim or wait?")
    if option == "wait":
        door = input("which door do u choose ,red  or blue or yellow")
        if door == "red " or door == "blue":
            print("game over")
        elif door == "yellow":
            print("you win")
        else:
            print("you chose invalid color")
    else:
        print("game over")

else:
    print("game over")

