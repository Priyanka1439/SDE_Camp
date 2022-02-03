"""
pattern 6: 

    *
   **
  ***
 ****
*****

"""
out = 5
for i in range(1, out + 1):
    print(end=" " * (out - i))
    print("*" * i)