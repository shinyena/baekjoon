n = int(input())

dp1 = {1:1, 2:0}
dp0 = {1:0, 2:1}
dp = {1:1, 2:1}

for x in range(3, n+1):
    dp1[x] = dp0[x-1]
    dp0[x] = dp1[x-1] + dp0[x-1]
    dp[x] = dp1[x] + dp0[x]

print(dp[n])