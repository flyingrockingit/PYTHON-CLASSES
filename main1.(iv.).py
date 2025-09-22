file = open ('AAR.txt','a')
file.write(f"My name is AVNI ROY \n I am eigtheen years old \n I am currently studying at Murdoch University Dubai where  I am pursuing foundation program in Infromation Technology \n My hobbies are sleeping, watching movies, coding, eating, cooking as well as baking \n I love myself, family and friends dearly.")
file.close()

file = open('AAR.txt', 'r')
print (file.read())
file.close()