n = int(input())
grapes = {}
for i in range(1, n+1):
    grapes[i] = int(input())

dp = {}

if n >= 1:
    dp[1] = grapes[1]
if n >= 2:
    dp[2] = grapes[1] + grapes[2]
if n >= 3:
    dp[3] = max(grapes[1] + grapes[2], grapes[2] + grapes[3], grapes[1] + grapes[3])



for x in range(4, n+1):
    dp[x] = max(grapes[x] + grapes[x-1] + dp[x-3], grapes[x] + dp[x-2], dp[x-1])

print(dp[n])
