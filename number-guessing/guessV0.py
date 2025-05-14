import random as rd
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("WELCOME TO MY NUMBER GUESSING GAME")
print("SELECT THE RANGE")

while True:
    minRange = input("I SELECT (min) ")
    maxRange = input("I SELECT (max) ")
    if minRange.isdigit() and maxRange.isdigit() and int(maxRange) > int(minRange) and int(maxRange) is not int(minRange):
        clear()
        print("GOOD CHOICES, NOW WAIT WHILE I THINK...")
        break
    clear()
    print("BAD CHOICES CHOICES, SELECT AGAIN")

selectedNumber = rd.randint(int(minRange),int(maxRange))

time.sleep(2)
clear()
print("OKAY I'M READY. WHAT DID I CHOOSE? ("+str(minRange)+"-"+str(maxRange)+")")
playerAnswer = input("YOU CHOSE ")

if int(playerAnswer) is int(selectedNumber):
    print("YOU GOT IT, YOU'RE SO GOOD AT THIS GAME")
else:
    print("NO THATS WRONG, YOU'RE TRASH")
