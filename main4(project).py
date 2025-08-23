num = int(input("Enter a number: "))

num_str = str(num)
num_digits = len(num_str)

armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

if num == armstrong_sum:
    print(f"✅ {num} is an Armstrong number.")
else:
    print(f"❌ {num} is NOT an Armstrong number.")