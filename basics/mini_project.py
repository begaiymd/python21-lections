import random
number_guess = random.int(1,10)
times_guess = 0
username = input()
play = print("Do you want to play? yes or no")
answer = input()
while answer != "no":
    break
print("you can guess 2 times")
num1 = int(input("enter number between 1-10: "))
while times_guess < 2:
    if num1 != number_guess:
        print("try again")
        times_guess < 1
        num1 = int(input("enter number between 1-10: "))
        if num1 == number_guess:
            print ("you guessed the number")
        else:
            break
print("do you want to play again? yes or no")
if num1 == number_guess:
    print("you guessed the number")
else:
    print("end of the game")