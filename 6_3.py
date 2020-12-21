# 6.3 and 6.4 in same file
def tester(givenstring= "Too short"):

#Löytyykö X
    if givenstring.find("X") != -1:

        print(givenstring)
        print("X spotted!")
    else:
        print(givenstring)

def test():
    pass        

def main():

    test()

    while True:
        kir = input("Write something (quit ends):")
        if len(kir) >9:
            tester(kir)
        elif kir =="quit":
            exit()    
        else:
            tester()

main()