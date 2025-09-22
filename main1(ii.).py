# open a file in write mode
file = open('Codingal.txt', 'w')

print("OPENING FILE IN WRITE MODE...")

file.write("I have updated in write mode.")

file.close()

# open file in read mode
file = open('Codingal.txt', 'r')

print(f"OPENING FILE IN READ MODE:\n{file.read()}")

file.close()
