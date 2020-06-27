#Guessing Game

from random import randint

i = 1
count = 2
while i<=3:
    guess = int(input("Guess :"))
    i +=1
    num = randint(0, 10)
    if guess== num:
        print("You win")
        break
    else:
        print("You have " ,count , "left" )

        if count == 0:

            print("The Number was " ,num, ", please try gain")
        count -= 1
