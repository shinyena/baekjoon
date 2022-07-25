N = int(input())
arr = []
arr = list(map(int, input().split()))
brr = []
brr = list(map(int, input().split()))

arr.sort()
brr.sort(reverse=True)
sum = 0
for i in range(N):
    mul = arr[i]*brr[i]
    sum += mul
print(sum)
