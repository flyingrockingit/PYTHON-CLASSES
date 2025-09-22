file = open ('Codingal.txt','a')
print("OPENING FILE IN APPEND MODE...")
file.write("I have appended the text in this file.")
file.close

file=open('Codingal.txt', 'r')
print(file.read())
file.close