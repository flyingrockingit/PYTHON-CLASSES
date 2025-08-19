number=int(input("enter your number:"))
if number>1:
    for i in range(2,int (number**0.5)+1):
     if number%i==0:
        print (f"{number} is not a prime")
        break
    else:
        print (f"{number} is a prime")
else:   
   print (f"{number} isn't a prime")