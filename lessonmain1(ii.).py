def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

pupils = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynee Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

print("\nOriginal list of lists:")
for p in pupils:
    print(p)

print("\nConverted list to dictionary:")
converted = test(pupils)

for key, value in converted.items():
    print(f"{key}: {value}")
