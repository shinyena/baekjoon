T = int(input())

a = T//300
T %= 300

b = T//60
T %= 60

c = T//10
T %= 10

if T == 0:
    print(a, b, c)
else:
    print(-1)