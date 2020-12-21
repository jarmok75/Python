
def onko_numero(num):
    
    try:

        lis =int(num)
    except (TypeError, ValueError):
            print("The input was malformed.")
    
    else:
         print("The input was suitable!")

def avaa_tied(tied):

    try:
        handle = open(tied,"r")
        tulos =handle.readline()
        tulos2 = tulos.strip()
        #print(tulos2)
        luku = int(tulos2)
        #print(luku)
        
    except (NameError, FileNotFoundError):
            print("There seems to be no file with that name.")
        
    
    except (TypeError, ValueError):
        print("The file contents were unsuitable.")

    else:
        luku2 = 1000/luku
        print("The result was", luku2)








def main():

    #numero =input("Give a number:")
    #onko_numero(numero)
    tied = input("Give the file name:")
    avaa_tied(tied)


main()

