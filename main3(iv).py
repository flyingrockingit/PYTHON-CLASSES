num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
        if num % 2 == 0:
            print("It is even.")
        else:
            print("It is odd.")
else:
    print("The number is negative.")
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
