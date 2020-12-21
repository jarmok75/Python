import time

def alku():
    val =0
    
    while val !="4":

        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Quit")
        val = input("Please select one:")


        
        if val =="1":
            handle = open("notebook.txt","r")
            test = handle.readlines()
            for line in test:
                
                line2 = line.strip()
                print(line2)
                handle.close()
        

        if val =="2":
            handle = open("notebook.txt","a")
            lis = input("Write a new note:")
            handle.write(lis +":::" + time.strftime("%X %x") + "\n")
            handle.close()

        if val =="3":
            handle = open("notebook.txt","w")
            handle.close()
            print("Notes deleted.")

        if val =="4":
            print("Notebook shutting down, thank you.")
            exit()
    handle.close()


def main():
    alku()

main()