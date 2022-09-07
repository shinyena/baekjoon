n = int(input())

dp = []
for i in range(n):
    dp.append([])
    dp[i] = list(map(int, input().split()))

# print(dp)

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][0] += min(dp[i-1][1], dp[i-1][2])
        if j == 1:
            dp[i][1] += min(dp[i-1][0], dp[i-1][2])
        if j == 2:
            dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))