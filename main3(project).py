# Step 1: 
with open("FILESAMPLE2.txt", "a") as file:
    file.write("\nHello, my name is Avni. I am learning File Handling - Python currently.")

# Step 2:
with open("FILESAMPLE2.txt", "r") as file:   
    content = file.read()          
    words = content.split()        
    print("Words in the file:", words)

# Step 3: 
import os
print("Checking if the file exists...")
if os.path.exists("mMyFILE.txt"):
    print("This file exists already")
else:
    print("This file does not exist")

# Step 4:
with open("m_MYFile.txt", "a") as file:  
        file.write("\nHello, my name is AAR. This is my new created file.")

#Step 5:
if os.path.exists("Sample_File.txt"):
    os.remove("Sample_File.txt")
    print("Sample_File.txt deleted successfully.")
else:
    print("Sample_File.txt does not exist.")