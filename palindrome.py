a = int(input("Enter a number: "))
rev = 0
original=a
while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

if original==rev:
    print("the number is palindrome")
else:
    print("the number is not palindrome")


  
