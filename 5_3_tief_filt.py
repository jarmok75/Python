handle = open("facts.txt","r")
test = handle.readlines()
print("Following was read from the file:")
for i in test:
  print (i)

handle.close()