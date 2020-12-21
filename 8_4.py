import time
import os.path

def alku():
    val =0
    
    

    if os.path.isfile('notebook.txt'):
            #print ("Now using file notebook.txt")
            tied_nimi = "notebook.txt"
        # Do something with the file
    else:
            print("No default notebook was found, created one.")
            #print("Now using file notebook.txt")
            handle = open("notebook.txt","w")
            handle.close()
            tied_nimi = "notebook.txt"
            
            
    while val !="5":  

        
            
        print("Now using file", tied_nimi)
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Change the notebook")
        print("(5) Quit")
        val = input("Please select one:")


       



        
        if val =="1":
            handle = open(tied_nimi,"r")
            test = handle.readlines()
            for line in test:
                
                line2 = line.strip()
                print(line2)
                handle.close()
        

        if val =="2":
            handle = open(tied_nimi,"a")
            lis = input("Write a new note:")
            handle.write(lis +":::" + time.strftime("%X %x") + "\n")
            handle.close()

        if val =="3":
            handle = open(tied_nimi,"w")
            handle.close()
            print("Notes deleted.")

        if val =="4":
            tied_nimi =input("Give the name of the new file:")
            if os.path.isfile(tied_nimi):
                print("Now using file", tied_nimi)

            else:    
                handle2 = open(tied_nimi, "a")
                print("No notebook with that name detected, created one.")
                handle2.close()

        if val =="5":
            print("Notebook shutting down, thank you.")
            exit()
    handle.close()


def main():
    alku()

main()