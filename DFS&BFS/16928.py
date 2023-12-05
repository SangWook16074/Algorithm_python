import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
jump = {}
for _ in range(n+m):
    start, end = map(int, input().split())
    jump[start] = end
board = [0 for _ in range(101)]
visited = [False for _ in range(101)]
q = deque()
q.append(1)
visited[1] = True
while q:
    current = q.popleft()
    for i in range(1, 7):
        move = current + i
        if move <= 0 or move > 100:
            continue

        if move in jump.keys():
            move = jump[move]

        if not visited[move]:
            q.append(move)
            visited[move] = True
            board[move] = board[current] + 1
print(board[100])