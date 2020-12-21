import random
import math

#Kolikonheitto
def kh():

    number = random.randint(0,100)

    tulos = random.randint(0,1)

    if tulos ==1:
        print("Heads!")
    else:
        print("Tails!")

    

def main():

    kh()

main()