import random

def dices():
    d100 = random.randint(1,100)
    d20 = random.randint(1,20)
    d12 = random.randint(1,12)
    d8 = random.randint(1,8)
    d6 = random.randint(1,6)
    d4 = random.randint(1,4)
    return{
        "d100":d100,
        "d20":d20,
        "d12":d12,
        "d8":d8,
        "d6":d6,
        "d4":d4
    }
result = dices()
print(result["d4"])