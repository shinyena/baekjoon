import sys

sys.setrecursionlimit(10 ** 4)


n, m = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
def dfs(x, visited):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i, visited)

answer = 0
for i in range(1, n+1):
    if len(graph[i]) == 0:
        answer += 1
    else:
        for j in graph[i]:
            if not visited[j]:
                dfs(j, visited)
                answer += 1

print(answer)
