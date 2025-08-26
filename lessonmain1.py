# Lists

# empty
empty = []

# numbers
numbers = [1, 2, 3, 4, 23, 45, 453, 5532, 7, 443]

# strings
strings = ["I", "am", "going", "to", "University", "soon"]

# mixed
mixed = ["AAR", 7, 5, 2007, True]

print(f"mixed: {mixed}\nempty: {empty}\nnumbers: {numbers}\nstrings: {strings}")

# access element
print(strings[2])  

# append
numbers.append(100)      
strings.append("soon")   
mixed.append(False)      

print(f"\nAfter append:\nnumbers: {numbers}\nstrings: {strings}\nmixed: {mixed}")

# remove
numbers.remove(23)
strings.remove("I")

print(f"\nAfter remove:\nnumbers: {numbers}\nstrings: {strings}")

# pop
mixed.pop(1)
strings.pop(4)

print(f"\nAfter pop:\nmixed: {mixed}\nstrings: {strings}")

# reverse
numbers.reverse()
strings.reverse()
mixed.reverse()

print(f"\nAfter reverse:\nnumbers: {numbers}\nstrings: {strings}\nmixed: {mixed}")
