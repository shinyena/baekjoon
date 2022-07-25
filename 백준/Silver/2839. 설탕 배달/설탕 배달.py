N = int(input())

leaf = [(3,1), (5,1)]
while True:
    # print(leaf)
    if min(leaf[0]) > N:
        print(-1)
        exit()
    for (num, cnt) in leaf:
        if num == N:
            print(cnt)
            exit()
    tmp = []
    for (num, cnt) in leaf:
        tmp.append((num+3, cnt+1))
        tmp.append((num+5, cnt+1))
    leaf = list(set(tmp))