"""
pattern 9: 

*********
 *******
  *****
   ***
    *

"""
for i in range(6, 0, -1):
    for a in range(0, 6-i):
        print(" ", end="")
    for b in range(i, 2*i-1):
        print("*", end="")
    for c in range(1, i-1):
        print("*", end="")
    print()