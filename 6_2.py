
def poweroftwo(numero):
    tulos = 1

    for i in range(0,numero):

        tulos= tulos*2

    print("The result is ", tulos)

def main():

    num = int(input("Give a number:"))

    poweroftwo(num)

main()