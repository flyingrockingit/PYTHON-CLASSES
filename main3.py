with open ("SampleFile 2.txt", "w") as file:
    file.write("Hey! I am known as the most cutest animal:Panda.\n I am 5 years old currently")
with open ("SampleFile 2.txt", "r") as file:
    print (file.read())

with open ("SampleFile 2.txt", "r") as file:
    data=file.readlines()
    print("Words in this file are ....")
    for line in data:
        word=line.split()
        print (word)

