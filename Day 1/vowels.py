from numpy import character

value = input("Enter a single character: ")
value = value.lower()
if value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u':
    print(value + " is a vowel.")
else:
    print(value + " is not a vowel.")