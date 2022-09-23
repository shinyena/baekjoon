from collections import deque

d = [(1, 2), (2, 1), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]
def bfs(board, nx, ny, px, py, n):
    queue = deque([(nx, ny)])
    while True:
        (x, y) = queue.popleft()
        if (x,y) == (px, py):
            print(board[py][px])
            break
        for (dx, dy) in d:
            if 0<=x+dx<n and 0<=y+dy<n:
                if board[y+dy][x+dx] == 0:
                    board[y+dy][x+dx] = board[y][x] + 1
                    queue.append((x+dx, y+dy))

T = int(input())
for t in range(T):
    n = int(input())
    nx, ny = map(int, input().split())
    px, py = map(int, input().split())
    bfs([[0]*n for _ in range(n)], nx, ny, px, py, n)

