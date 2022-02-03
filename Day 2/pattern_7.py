"""
pattern 7:

*****
 ****
  ***
   **
    *

"""
out = 5
for i in range(out , 0, -1):
    print(end=" " * (out - i))
    print("*" * i)