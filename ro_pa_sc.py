import random

from click import option

user_win=0
computer_win=0

options=["rock", "paper", "scissors"]


while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit\n").lower()

    if user_input=="q":
        break

    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    #rock:0, paper: 1, scissors:2
    computer_pick=options[random_number]
    print("Computer Picked", computer_pick)

    if user_input=="rock" and computer_pick=="scissors":
        print("You won!!")
        user_win+=1
        continue

    elif user_input=="paper" and computer_pick=="rock":
        print("You won!!")
        user_win+=1
        continue

    elif user_input=="scissors" and computer_pick=="paper":
        print("You won!!")
        user_win+=1
        continue

    else:
        print("You Lost!!")
        computer_win+=1

print("you won ", user_win, "times")
print("computer won ", computer_win, "times")

print("Goodbye!!!")