import sys
sys.setrecursionlimit(10 ** 4)

n = int(input())
colors = []

for i in range(n):
    colors.append([])
    colors[i] = list(input())

blindness = []
for i in range(n):
    blindness.append([])
    for j in range(n):
        if colors[i][j] == "R":
            blindness[i].append("G")
        else:
            blindness[i].append(colors[i][j])

visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


def dfs1(x, y, color):
    visited1[y][x] = True
    for (dx, dy) in d:
        if 0<=x+dx<n and 0<=y+dy<n:
            if not visited1[y+dy][x+dx] and colors[y+dy][x+dx] == color:
                dfs1(x+dx, y+dy, color)

def dfs2(x, y, color):
    visited2[y][x] = True
    for (dx, dy) in d:
        if 0<=x+dx<n and 0<=y+dy<n:
            if not visited2[y+dy][x+dx] and blindness[y+dy][x+dx] == color:
                dfs2(x+dx, y+dy, color)



answer1 = 0
for h in range(n):
    for w in range(n):
        if not visited1[h][w] and colors[h][w] == "R":
            dfs1(w, h, "R")
            answer1 += 1
        if not visited1[h][w] and colors[h][w] == "G":
            dfs1(w, h, "G")
            answer1 += 1
        if not visited1[h][w] and colors[h][w] == "B":
            dfs1(w, h, "B")
            answer1 += 1

answer2 = 0
for h in range(n):
    for w in range(n):
        if not visited2[h][w] and blindness[h][w] == "G":
            dfs2(w, h, "G")
            answer2 += 1
        if not visited2[h][w] and blindness[h][w] == "B":
            dfs2(w, h, "B")
            answer2 += 1


print(answer1, answer2)
