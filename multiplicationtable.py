
n = int(input("Enter a number: "))

print("Multiplication table of", n, "is:")

for num in range(1, 11):
    table = num * n
    print(num, "x", n, "=", table)
