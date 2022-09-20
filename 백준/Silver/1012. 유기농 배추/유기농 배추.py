import sys

sys.setrecursionlimit(10 ** 4)

T = int(input())
cabbage = []

for i in range(T):
    M, N, K = map(int, input().split())
    cabbage.append([])
    for j in range(N): # N이 세로 길이
        cabbage[i].append([])
        for k in range(M): # M이 가로 길이
            cabbage[i][j].append(0)
    for _ in range(K):
        x, y = map(int, input().split()) # (x, y) = (가로, 세로)
        cabbage[i][y][x] = 1

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = []

for i in range(len(cabbage)):
    visited.append([])
    for j in range(len(cabbage[i])):
        visited[i].append([])
        for k in range(len(cabbage[i][j])):
            visited[i][j].append(False)

def dfs(x, y, t, m, n):
    visited[t][y][x] = True
    for (dx, dy) in d:
        if 0<=x+dx<m and 0<=y+dy<n:
            if cabbage[t][y+dy][x+dx] == 1 and not visited[t][y+dy][x+dx]:
                dfs(x+dx, y+dy, t, m, n)

for t in range(T):
    answer = 0
    for y in range(len(cabbage[t])):
        for x in range(len(cabbage[t][y])):
            if cabbage[t][y][x] == 1 and not visited[t][y][x]:
                dfs(x, y, t, len(cabbage[t][y]), len(cabbage[t]))
                answer += 1
    print(answer)