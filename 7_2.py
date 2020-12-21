import random
import math
def kps():
    rounds =0
    tie = 0
    comp_won = 0
    you_won = 0
    val = "test"

    while True:
                
                val =input("Foot, Nuke or Cockroach? (Quit ends):") 
                if val =="Quit":
                        print("You played", rounds,"and won",you_won, "playing tie in", tie, "rounds.")
                        exit()
                print("You chose:", val)
                val_comp = random.randint(0,2)
                #O = nuke
                #1 = Cockroach
                #2 = Foot
                #print("Computer chose:", val_comp)

            #Computer Nuke

                if val_comp ==0 and val =="Nuke":
                    print("Computer chose: Nuke")
                    print("It is a tie!")
                    tie = tie +1
                    rounds = rounds +1
                    
                elif val_comp ==0 and val =="Cockroach":
                    print("Computer chose: Nuke")
                    print("You LOSE!")
                    rounds = rounds +1
                    comp_won = comp_won +1
                
                elif val_comp ==0 and val =="Foot":
                    print("Computer chose: Nuke")
                    print("You LOSE!")
                    rounds = rounds +1
                    comp_won = comp_won +1

            #Computer Cockroach
                elif val_comp ==1 and val =="Nuke":
                    print("Computer chose: Cockroach")
                    print("You WIN!")
                    rounds = rounds +1
                    you_won = you_won +1



                elif val_comp ==1 and val =="Cockroach":
                    print("Computer chose: Cockroach")
                    print("It is a tie!")
                    tie = tie +1
                    rounds = rounds +1

                elif val_comp ==1 and val =="Foot":
                    print("Computer chose: Cockroach")
                    print("You WIN!")
                    you_won = you_won +1
                    rounds = rounds +1 
            #Computer Foot:
                elif val_comp ==2 and val =="Nuke":
                    print("Computer chose: Foot")
                    print("You WIN!")
                    rounds = rounds +1
                    you_won = you_won +1
                elif val_comp ==2 and val =="Cockroach":
                    print("Computer chose: Foot")
                    print("You LOSE!")
                    rounds = rounds +1
                    comp_won = you_won +1

                elif val_comp ==2 and val =="Foot":
                    print("Computer chose: Foot")
                    print("It is a tie!")
                    rounds = rounds +1
                    tie = tie +1


                


def main():

    kps()

main()