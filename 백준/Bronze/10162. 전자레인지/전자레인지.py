T = int(input())
a, b, c = 0, 0, 0
if T>=300:
    a = T//300
    T %= 300
if T>=60:
    b = T//60
    T %= 60
if T>=10:
    c = T//10
    T %= 10
if T == 0:
    print(a, b, c)
else:
    print(-1)