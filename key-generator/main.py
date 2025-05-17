# made by lunatronia with sarcasm, because this shit will not work and is made as a joke.

import random as rd
import string as st

def sectionMaker():
    random_string = ''.join(rd.choices(st.ascii_uppercase + st.digits, k=5))
    return random_string

def fivexfive():
    print(sectionMaker()+"-"+sectionMaker()+"-"+sectionMaker()+"-"+sectionMaker()+"-"+sectionMaker())

def fivexthree():
    print(sectionMaker()+"-"+sectionMaker()+"-"+sectionMaker())

print("\n\033[93mDISCLAIMER: this will not work, this is really stupid and don't waste your time on this. this was made as a joke.\n")

print("\033[95mhi, what length? (1||2)\n(1) 5x3\n(2) 5x5")

while True:
    keyType = input(">")
    if int(keyType) == 1 or int(keyType) == 2 and keyType.isdigit() == 1:
        break
    else:
        print("incorrect selection")

print("how many tries? (0>)")

while True:
    trySetAmount = input(">")
    if trySetAmount.isdigit() == 1 and int(trySetAmount) > 0:
        tryAmount = 0
        break
    else:
        print("incorrect selection")

if int(keyType) == 1:
    while tryAmount < int(trySetAmount):
        fivexthree()
        tryAmount += 1

elif int(keyType) == 2:
    while tryAmount < int(trySetAmount):
        fivexfive()
        tryAmount += 1

