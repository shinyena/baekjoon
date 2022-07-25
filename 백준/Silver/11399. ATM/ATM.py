N = int(input())
arr = []
arr = list(map(int, input().split()))
arr.sort()

brr = []
sum = 0
for n in arr:
    sum += n
    brr.append(sum)

answer = 0
for n in brr:
    answer += n

print(answer)