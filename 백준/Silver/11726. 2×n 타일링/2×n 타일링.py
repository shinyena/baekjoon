n = int(input())
dp = {1:1, 2:2}

def fn(x):
    if x in dp:
        return dp[x]
    else:
        dp[x] = fn(x-1) + fn(x-2)
        return dp[x]

print(fn(n)%10007)
