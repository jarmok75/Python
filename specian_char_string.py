import re 

string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')


handle = open("strings.txt","r")
test = handle.readlines()
#print("Following was read from the file:")

"""
for i in  test:
    if(string_check.search(i) == None): 
        print (i , "was ok.", end=" " )
    else:
        print(i , "was invalid.", end=" ")
"""
print(handle.readlines())
 
handle.close()