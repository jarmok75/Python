
import re 

string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:ö+-]')

handle = open("strings.txt","r")

test = handle.readlines()

#print("Following was read from the file:")

for i in test:
    i2 = i.strip()
    if(string_check.search(i2) ==None): 

        print (i2,"was ok.")

    else:

        print(i2,"was invalid.")


handle.close()

