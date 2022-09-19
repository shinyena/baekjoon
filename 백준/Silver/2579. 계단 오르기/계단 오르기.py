n = int(input())
stairs = {}
for i in range(1, n+1):
    stairs[i] = int(input())

dp = {}

def fn(x):
    if x == 1:
        dp[x] = stairs[1]
    if x == 2:
        dp[x] = stairs[1] + stairs[2]
    if x == 3:
        dp[x] = max(stairs[1], stairs[2]) + stairs[3]
    if x in dp:
        return dp[x]
    else:
        dp[x] = max(stairs[x] + stairs[x-1] + fn(x-3), stairs[x] + fn(x-2))
        return dp[x]

print(fn(n))
