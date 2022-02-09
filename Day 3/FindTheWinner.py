n = 5
k = 2
dp = [x for x in range(1,n+1)]
pointer = 0
count = 1
while len(dp) > 1:
    if count == k:
        dp.pop(pointer)
        count = 1
    else:
        count += 1
        pointer += 1
        pointer = pointer % len(dp)
print(dp[0])