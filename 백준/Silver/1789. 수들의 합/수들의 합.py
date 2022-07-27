s = int(input())

sum = 0
i = 1
while True:
    sum += i
    if sum>s:
        print(i-1)
        break
    if sum == s:
        print(i)
        break
    i += 1
