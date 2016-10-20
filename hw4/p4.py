#Steven Kravitsky
#12586350
#Assignment 4
#Problem 4

import random

def roll():
    dice = 5
    counter = 0
    while dice != 0:
        for i in range(dice):
            x = random.randint(1,6)
            if x==6:
                dice = dice - 1
        counter = counter + 1
    return counter	

if __name__ == '__main__':
    sum = 0
    numrolls = 1000
    total = 0
    for i in range(numrolls):
        x = roll()
        sum = sum + x
    total = sum / numrolls
    print total
