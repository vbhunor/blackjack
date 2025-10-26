#Blackjack basic Python terminal game made by Vigh-Bucz Hunor 2025. 10. 26.
from random import randint, choice
input("Üdvözöllek a blackjack játékban! Nyomj egy gombot a kezdéshez...\n")
def lapjaim():
    x = randint(1, 11)
    y = randint(1, 11)
    ossz = x + y
    if ossz == 21:
        print("Te nyertél!")
    elif ossz == 22:
        ossz -= 10
    print(f"A te lapjaid {x} és {y}, a lapjaid összértéke: {ossz}\n")
    return ossz

def oszto_lapjai():
    x = randint(1, 11)
    y = randint(1, 11)
    ossz1 = x + y
    if ossz1 == 21:
        print("Sajnálom, az osztó nyert")
    elif ossz1 == 22:
        ossz1 -= 10
    print(f"Az osztó lapjai {x} és ###, a lapjaid összértéke nem ismert\n")
    return ossz1

def jatek():
    ossz = lapjaim()
    ossz1 = oszto_lapjai()    
    while True:
        a = input("Lapkérés (L) vagy tartózkodás (O)").upper()
        while ossz1 < 17:
            z = randint(1, 11)
            if z == 11 and ossz1 + z > 21:
                z = 1    
            ossz1 = ossz1 + z
            if ossz1 > 21:
                ossz1 -= randint(1, 10)
            
        if a == "L":
            z = randint(1, 11)
            if z == 11 and ossz + z > 21:
                z = 1    
            ossz = ossz + z
            print(f"Az új kártyád értéke {z}, a lapjaid összege {ossz}")
            if ossz > 21:
                return f"Sajnálom, az osztó nyert. A lapjaid összértéke: {ossz}"
                
            if ossz == 21:
                return f"Gratulálok! Te nyertél! A lapjaid összértéke pontosan {ossz}! "
                
        elif a == "O":  
            if ossz > ossz1:
                return f"Gratulálok, te nyertél! {ossz}>{ossz1}"
            elif ossz == ossz1:
                return f"Döntetlen! {ossz} = {ossz1} "
            else:
                return f"Sajnálom, az osztó nyert, {ossz1}>{ossz}"
        else:
            print("O vagy L gombot nyomj meg!")
while True:
    print(jatek())
    ujra = input("Szeretnél újra játszani? (I/N): \n").upper()
    if ujra != "I":
        print("Köszönöm a játékot! Viszlát!")
        break
