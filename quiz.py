print("Welcome to your Computer quiz")

playing=input("Do ypu want to play? ") 

if (playing.lower()!="yes"):
    quit()

print("Okay!! Let's Play")
score= 0

answer = input("What does CPU stands for? \n")
if answer.lower()== "central processing unit":
    print("Correct")
    score+=1
else:
    print("!!!!!Incorrect!!!!")


answer = input("What does GPU stands for? \n")
if answer.lower()== "graphic processing unit":
    print("Correct")
    score+=1
else:
    print("!!!!!Incorrect!!!!")


answer = input("What does RAM stands for? \n")
if answer.lower()== "random access memory":
    print("Correct")
    score+=1
else:
    print("!!!!!Incorrect!!!!")


answer = input("What does PSU stands for? \n")
if answer.lower()== "power supply unit":
    print("Correct")
    score+=1
else:
    print("!!!!!Incorrect!!!!")

print("you got "+ str(score)+ " Question correct!")
print("you got "+ str((score/4)*100)+ "%")