n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = {1:1, 2:2, 3:4}

def fn(x):
    if x in dp:
        return dp[x]
    else:
        return fn(x-1)+fn(x-2)+fn(x-3)

for a in arr:
    print(fn(a))
