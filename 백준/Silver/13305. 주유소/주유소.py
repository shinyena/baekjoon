n = int(input())
bridge = []
bridge = list(map(int, input().split()))
city = []
city = list(map(int, input().split()))
city.pop()

i = 0
now = i
answer = 0
while i != n-1:
    if city[now] > city[i]:
        now = i
    # print(bridge[i], city[now])
    answer += bridge[i]*city[now]
    i += 1
print(answer)
