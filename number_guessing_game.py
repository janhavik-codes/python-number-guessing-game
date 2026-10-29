import random

targetNUM= random.randint(1,100)
while True:
    userChoice = input("Enter a number between 1 and 100 or Quit:")
    if userChoice.upper() == "QUIT" :
        print("Better Luck Next time!")
        break
    try:
     userChoice = int(userChoice)
     if userChoice < 1 or userChoice > 100 :
         print("Invalid Choice!, please enter a number between 1 and 100")
     elif userChoice == targetNUM :

        print("You win!")
        break
     elif userChoice < targetNUM :
        print("Number is smaller than target,take a higher guess...")
     elif userChoice > targetNUM :
        print("Number is higher than target,take a smaller guess...")
    except ValueError:
        print("Invalid Choice!,please enter valid number or quit to exit")

print("---GAME OVER---")
print("Thank you for playing")