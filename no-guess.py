import random

top_of_range= int(input("Type a Number: "))

if top_of_range<=0:
    print("PLease enter a larger number than zero")
    quit()


random_number=random.randint(0,top_of_range)
print(random_number)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a Guess:  ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time ")
        continue

    if user_guess==random_number:
        print("You got it!!")
        break
    elif user_guess> random_number:
            print("You are above the number!")
    else:
            print("Youe are below the number!")
            
print("you got it in ", guesses, " guesses")