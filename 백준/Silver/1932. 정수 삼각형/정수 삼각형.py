n = int(input())
arr = []
for i in range(n):
    arr.append([])
    arr[i] = list(map(int, input().split()))

dp = []
for i in range(n):
    dp.append([])
    for j in range(len(arr[i])):
        dp[i].append(arr[i][j])


for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == len(arr[i]) - 1:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))