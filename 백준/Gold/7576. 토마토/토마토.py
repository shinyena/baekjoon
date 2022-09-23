from collections import deque

M, N = map(int, input().split())
tomatoes = []
for i in range(N):
    tomatoes.append([])
    tomatoes[i] = list(map(int, input().split()))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False]*M for _ in range(N)]


queue = deque([])

for y in range(N):
    for x in range(M):
        if tomatoes[y][x] == 1:
            queue.append((x, y))

while queue:
    (x, y) = queue.popleft()
    visited[y][x] = True
    for (dx, dy) in d:
        if 0<=x+dx<M and 0<=y+dy<N:
            if not visited[y+dy][x+dx] and tomatoes[y+dy][x+dx] == 0:
                tomatoes[y+dy][x+dx] = tomatoes[y][x] + 1
                queue.append((x+dx, y+dy))

if any(0 in t for t in tomatoes):
    print(-1)
else:
    print(max(map(max, tomatoes))-1)



