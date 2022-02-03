def Calculator(a, b, choice):
    switcher = {
        1 : a + b,
        2 : a - b,
        3 : a * b,
        4 : a / b
    }
    return switcher.get(choice, "Invalid Choice! Please try again.")

print("Simple Calculator")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = int(input("Enter your Choice: "))
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("Answer is " + str(Calculator(a, b, choice)))