def atioRecursive(string, num):
    if len(string) == 1:
        return int(string) + (num * 10)
    num = int(string[0:1]) + (num * 10)
    return atioRecursive(string[1:], num)

string = "112"
print(atioRecursive(string, 0))