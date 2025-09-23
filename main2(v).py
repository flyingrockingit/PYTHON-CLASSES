file = open("CS CODE.txt" ,"r")
line = file.readlines ()
file.close()
for i in range (2,5):
    print (line[i].strip())