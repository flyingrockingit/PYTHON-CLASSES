# No.1
file = open("Sample_File.txt", "r")    
print("File Contents:")               
print(file.read())                     
file.close()                           

#No.2
file = open("Sample_File.txt", "w")   
file.write ("Hey, my name is AVNI ROY. I am currently learning FILE HANDLING in Python.") 
file.close()

#No.3
file = open("Sample_File.txt", "a")   
file.write ("My favorite subject has to be Mathematics.\n")
file.close()

#No.4
file = open("Sample_File.txt", "r")   
print("Final File Contents:")
print(file.read())                     
file.close()                          
