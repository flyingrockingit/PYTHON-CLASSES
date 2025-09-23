file = open('CS CODE.txt', 'r')
lines = file.readlines ()
key_word = "I am 18."
file.close()

file = open('Codingal.txt', 'w')
for line in lines: 
    if not line.startswith ("I am 18."): 
        file.write (line)
file.close ()
