def revString(str_val, i, res):
    if i >= 0:
        res.append(str_val[i])
        revString(str_val, i-1, res)
    return res      

s = ["h","e","l","l","o"]
i = len(s) - 1
res = []
out = revString(s, i, res)
print(out)