import sys

sys.setrecursionlimit(10 ** 4)


d = [(1,0), (0,1), (-1,0), (0,-1), (1, 1), (-1,-1), (1,-1), (-1,1)]

def dfs(y, x, graph, visited):
    visited[y][x] = True
    for (dx, dy) in d:
        if 0<=x+dx<len(graph[0]) and 0<=y+dy<len(graph):
            if not visited[y+dy][x+dx] and graph[y+dy][x+dx] == 1:
                dfs(y+dy, x+dx, graph, visited)

def answer(graph, w, h):
    answer = 0
    visited = [[False]*w for _ in range(h)]

    for height in range(h):
        for width in range(w):
            if not visited[height][width] and graph[height][width] == 1:
                dfs(height, width, graph, visited)
                answer += 1
    return answer

while True:
    graph = []
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append([])
        graph[i] = list(map(int, input().split()))
    print(answer(graph, w, h))

