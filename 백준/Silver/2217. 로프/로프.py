n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

i = 0
answer = 0
while True:
    if n == 0:
        print(answer)
        break
    if arr[0]*n > answer:
        answer = arr[0]*n
    n -= 1
    arr.pop(0)