file = open("CS CODE.txt" ,"a")
print ("Opening the file using Appended mode")
file.write (f" I am AVNI ABANINDRA ROY.\n I am 18 years old.")
file.close()

file = open('CS CODE.txt', 'r')
print (file.read())
file.close()
