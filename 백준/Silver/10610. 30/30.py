n = input()
numbers = "".join(n)
numbers = [int(i) for i in numbers]
numbers.sort(reverse=True)

if 0 in numbers:
    sum = 0
    for i in numbers:
        sum += i
    if sum % 3 != 0:
        print(-1)
    else:
        print(int("".join(str(s) for s in numbers)))
else:
    print(-1)