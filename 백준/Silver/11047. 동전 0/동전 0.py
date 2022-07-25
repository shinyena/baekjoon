N, K = map(int, input().split())
arr = []
for _ in range(N):
    m = int(input())
    arr.append(m)
arr.sort(reverse=True)
# print(arr)

i = 0
cnt = 0
while K != 0:
    if arr[i] > K:
        i += 1
    else:
        cnt += K//arr[i]
        K %= arr[i]
print(cnt)