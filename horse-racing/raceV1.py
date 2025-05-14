import random as rd
import os
import time

print("-------------")
print("WELCOME TO HORSE RACING!!!!")
print("SELECT A HORSE TO START (1-4)")
print("-------------")
selectedHorse = input()
print("-------------")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while not selectedHorse.isdigit() or int(selectedHorse) not in range(1,5):
    print("WRONG SELECTION SELECT AGAIN")
    print("-------------")
    selectedHorse = input()
else:
    print("YOU HAVE SELECTED HORSE NO. "+str(selectedHorse))
    
print("THE MATCH IS ABOUT TO START...")
print("-------------")

global horseOne
global horseTwo
global horseThree
global horseFour
global horseMovement

round = 0
horseOne = 0
horseTwo = 0
horseThree = 0
horseFour = 0
horses = [horseOne, horseTwo, horseThree, horseFour]

time.sleep(1.5)

horseMovement = rd.randint(0,3)


def movement(horseMovement):
    
    global horseOne, horseTwo, horseThree, horseFour
    
    match horseMovement:
        case 0:
            horseOne = horseOne+1
        case 1:
            horseTwo = horseTwo+1
        case 2:
            horseThree = horseThree+1
        case 3:
            horseFour = horseFour+1

while 7 not in horses:
    
    time.sleep(0.5)
    
    horseMovement = rd.randint(0,3)
    movement(horseMovement)
    horses = [horseOne, horseTwo, horseThree, horseFour]
    round = round+1
    clear()

    match horseOne:
        case 0:
            print("1. |o-------|")
        case 1:
            print("1. |-o------|")
        case 2:
            print("1. |--o-----|")
        case 3:
            print("1. |---o----|")
        case 4:
            print("1. |----o---|")
        case 5:
            print("1. |-----o--|")
        case 6:
            print("1. |------o-|")
        case 7:
            print("1. |-------o|")
        
    match horseTwo:
        case 0:
            print("2. |o-------|")
        case 1:
            print("2. |-o------|")
        case 2:
            print("2. |--o-----|")
        case 3:
            print("2. |---o----|")
        case 4:
            print("2. |----o---|")
        case 5:
            print("2. |-----o--|")
        case 6:
            print("2. |------o-|")
        case 7:
            print("2. |-------o|")
        
    match horseThree:
        case 0:
            print("3. |o-------|")
        case 1:
            print("3. |-o------|")
        case 2:
            print("3. |--o-----|")
        case 3:
            print("3. |---o----|")
        case 4:
            print("3. |----o---|")
        case 5:
            print("3. |-----o--|")
        case 6:
            print("3. |------o-|")
        case 7:
            print("3. |-------o|")
        
    match horseFour:
        case 0:
            print("4. |o-------|")
        case 1:
            print("4. |-o------|")
        case 2:
            print("4. |--o-----|")
        case 3:
            print("4. |---o----|")
        case 4:
            print("4. |----o---|")
        case 5:
            print("4. |-----o--|")
        case 6:
            print("4. |------o-|")
        case 7:
            print("4. |-------o|")
    print("-------------")

print("RACE ENDED,")

if horses[int(selectedHorse)-1] == 7:
    print("YOU WIN!!!")
else:
    print("YOU LOST!!!")
print("-------------")
