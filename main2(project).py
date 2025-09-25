# Task 1: Open the file and print the contents
file = open("SampleFile 2.txt", "r")
content = file.read()
print("**Contents of the file:**")
print(content)
file.close()  # Close after reading

# Task 2: Print the first 10 characters
file = open("SampleFile 2.txt", "r")
first_10 = file.read(10)
print("\n**First 10 characters:**")
print(first_10)
file.close()

# Task 3: Print the first line
file = open("SampleFile 2.txt", "r")
first_line = file.readline()
print("\n**First line:**")
print(first_line)
file.close()

# Task 4: Print the first four lines
file = open("SampleFile 2.txt", "r")
print("\n**First four lines:**")
for i in range(4):
    line = file.readline()
    if line == "":
        break
    print(line, end="")
file.close()

# Task 5: Loop through all lines one by one
file = open("SampleFile 2.txt", "r")
print("\n**All lines printed one by one:**")
for line in file:
    print(line, end="")
file.close()