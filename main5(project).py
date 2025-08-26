nterms = int(input("Enter the number of terms in Fibonacci series: "))

n1, n2 = 0, 1

print("Fibonacci series: ", end="")
print(f"{n1}, {n2}", end="")

for i in range(nterms - 2):
    n3 = n1 + n2
    print(f", {n3}", end="")
    n1, n2 = n2, n3