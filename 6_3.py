
def tester(givenstring= "Too short"):
    print(givenstring)

def main():

    while True:
        kir = input("Write something (quit ends):")
        if len(kir) >9:
            tester(kir)
        elif kir =="quit":
            exit()    
        else:
            tester()

        

main()