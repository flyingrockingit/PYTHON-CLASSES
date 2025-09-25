#new = open ("newFILE.txt", "x")
#new.close()

import os
print ("Checking if the file exists...")
if os.path.exists("newFILE.txt"):
    print("This file exists already")
else:
    print ("This file doesn't exist")

with open("newFILE.txt", "w") as f:
    f.write("Hello, this is my first line in the file!")

print("Line written to newFILE.txt successfully.")
