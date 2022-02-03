print("Largest of 3 numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a >= b and a >= c:
    print(str(a) + " is greater.")
elif b >= a and b >= c:
    print(str(b) + " is greater.")
else:
    print(str(c) + " is greater.")