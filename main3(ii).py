weight = int(input("Please enter your weight in kgs: "))
height = int(input("Please enter your height in cm: "))

BMI = weight / (height / 100) ** 2
print(f"Your BMI is {BMI}")

if BMI <= 18.0:
    print("You are underweight")
elif BMI <= 24.9:
    print("You have a normal weight")
elif BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese")
