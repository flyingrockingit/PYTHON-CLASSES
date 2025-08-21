def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print ("zero divison error!!")
    else:
        return a/b
while True:
    print("\nChoose an operation:\n1. Add\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice=input("please enter your choice:")
    if choice=="1":
        a=float(input("enter the first number:"))
        b=float (input("enter your second number:"))
        result=add(a,b)
        print (f"Results:{result}")
    elif choice=="2":
        a=float(input("enter the first number:"))
        b=float (input("enter your second number:"))
        result=sub(a,b)
        print (f"Results:{result}")
    elif choice=="3":
        a=float(input("enter the first number:"))
        b=float (input("enter your second number:"))
        result=mult(a,b)
        print (f"Results:{result}")
    elif choice=="4":
        a=float(input("enter the first number:"))
        b=float (input("enter your second number:"))
        result=divide(a,b)
        print (f"Results:{result}")
    elif choice=="5":
        print("Thank You for using AAR calulcator")
        break
    else:
        print("Wrong Input")