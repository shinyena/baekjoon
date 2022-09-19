a = int(input())
answers = []
for i in range(a):
    answers.append(int(input()))

dp = {1:1, 2:1, 3:1, 4:2, 5:2}
def fn(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = fn(n-5) + fn(n-1)
        return dp[n]

for answer in answers:
    print(fn(answer))