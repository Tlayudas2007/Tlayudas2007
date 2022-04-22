print("welcome to Diego's Guessing game \n -HINT every game will have different answers so no question will have the same number unless it is chosen agian")

import time
import random
z = random.randint(0,5)
y = random.randint(1,2)
time.sleep(3)
x = int(input("Guess the correct number \nhint: is less than 6 and more than 0 "))
print("Loading")
if(x == z):
    time.sleep(y)
    print("You guessed the right number")
else:
    time.sleep(z)
    print("Better luck next time")
if(x == z):
    i = int(input("Guess the right number \n Hint: the number is more than 10 and less than 20 "))
    c = random.randint(10,21)
    if(i == c):
        time.sleep(y)
        print(" YOU GUESSED THE RIGHT NUMBER")
        time.sleep(1)
        print("Please wait for approxamatly 5 secconds for the next one")
        time.sleep(5)
        x = int(input("Guess the right number \n: hint the number is more than 6 and less than 13"))
        s = random.randint(6,12)
        if(x == s):
            time.sleep(y)
            print("Wow thats really impressive of you to guess this far ")
        else:
            print("Welp you almost finished the game")    
    else:
        time.sleep(y)
        print("(.)(.)\n \_/\n You beat the game thats really cool not even Diego could finish his own game\n God Bless you for taking the time to finish this game")