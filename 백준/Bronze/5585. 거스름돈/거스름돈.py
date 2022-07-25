n = int(input())
n = 1000 - n

arr = [500, 100, 50, 10, 5, 1]

i = 0
cnt = 0

while n != 0:
    if n>=arr[i]:
        cnt += n // arr[i]
        n %= arr[i]
    else:
        i += 1

print(cnt)