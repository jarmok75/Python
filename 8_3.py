import math

def onko_numero():

    while True:
    
        try:

            num1 = int(input("Give a number:"))
        except (TypeError, ValueError):
                print("This input is invalid.")
        
        else:
            return num1



def main():
    sel = 0
    num = False
    print("Calculator")

    while sel !=8:


            
                if num == False:

                    l1 = onko_numero()
                    l2 = onko_numero()
                    
                    num = True

                print("(1) +")
                print("(2) -")
                print("(3) *")
                print("(4) /")
                print("(5) sin(number1/number2)")
                print("(6) cos(number1/number2)")


                print("(7) Change numbers")
                print("(8) Quit")
                
                print("Current numbers:", l1,l2)


                sel = int(input("Please select something (1-6):") )



                if sel !=1 and sel !=2 and sel !=3 and sel != 4 and sel != 5 and sel != 6 and sel!=7 and sel !=8 :

                    print("Selection was not correct.") 

                if sel == 1:
                    print("The result is:", l1+l2)

                if sel == 2:
                    print("The result is:", l1-l2)

                if sel == 3:
                    print("The result is:", l1*l2)
                if sel == 4:
                    l3 = l1/l2
                    print("The result is:", l3)
                if sel == 5:
                    l4 = math.sin(l1/l2)
                    print("The result is:", l4)
                    
                if sel == 6:
                    l5 = math.cos(l1/l2)
                    print("The result is:", l5)



                if sel == 7:
                    num = False
                    l1 = int(input("Give the first number:"))
                    l2 = int(input("Give the second number:"))
                    num = True

                
                if sel == 8:
                    print("Thank you!")
                    exit()




    print("Thank you!")
    exit()
main()