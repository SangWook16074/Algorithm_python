import sys
from collections import deque
input = sys.stdin.readline

def point(x, y):
    if y == 1:
        return (0, x)
    elif y == 2:
        return (height, x)
    elif y == 3:
        return (x, 0)
    elif y == 4:
        return (x, width)

def bfs(x, y, target_x, target_y):
    visited = [[0 for _ in range(width+1)] for _ in range(height + 1)]
    q = deque()
    visited[y][x] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > width or ny < 0 or ny > height or visited[ny][nx] != 0:
                continue

            if nx == 0 or nx == width or ny == 0 or ny == height:
                visited[ny][nx] = visited[y][x] + 1
                if nx == target_x and ny == target_y:
                    return visited[ny][nx] - 1
                else:
                    q.append((nx, ny))
    

current = (0, 0)
width, height = map(int, input().split())
graph = [[0 for _ in range(width+1)] for _ in range(height+1)]
target = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
for i in range(1, n+1):
    y, x = map(int, input().split())
    target.append(point(x, y))

my_y, my_x = map(int, input().split())
if my_y == 1:
    current = (my_x, 0)
elif my_y == 2:
    current = (my_x, height)
elif my_y == 3:
    current = (0, my_x)
elif my_y == 4:
    current = (width, my_x)

result = 0
for t in target:
    target_y, target_x = t
    x, y = current
    result += bfs(x, y, target_x, target_y)
print(result)