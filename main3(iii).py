import os
os.remove("newFILE.txt")
print ("Checking if the file exists...")
if os.path.exists("newFILE.txt"):
    print("This file exists already")
else:
    print ("This file doesn't exist")


