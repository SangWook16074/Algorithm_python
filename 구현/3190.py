import sys
from collections import deque
input = sys.stdin.readline

info = []
move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    apple = list(map(int, input().split()))
    graph[apple[0] - 1][apple[1] - 1] = 1

for _ in range(int(input())):
    x, c = input().split()
    info.append([int(x), c])

idx = 0
time = 0
snake = deque()
snake.append((0, 0))
direction = 0
while True:
    time += 1
    if idx < len(info):
        if time == info[idx][0]+1:
            # 0 = 오른쪽
            # 1 = 왼쪽
            # 2 = 위쪽
            # 3 = 아래쪽
            # 오른쪽일 경우
            if direction == 0:
                # 위
                if info[idx][1] == "L":
                    direction = 2
                # 아래
                else:
                    direction = 3
            # 왼쪽일 경우
            elif direction == 1:
                # 아래
                if info[idx][1] == "L":
                    direction = 3
                # 위
                else:
                    direction = 2
            # 위
            elif direction == 2:
                # 왼쪽
                if info[idx][1] == "L":
                    direction = 1
                # 오른쪽
                else:
                    direction = 0
            # 아래
            elif direction == 3:
                # 오른쪽
                if info[idx][1] == "L":
                    direction = 0
                # 왼쪽
                else:
                    direction = 1
            idx += 1

    x, y = snake[0][0], snake[0][1]
    nx, ny = x + move[direction][0], y + move[direction][1]
    # 벽을 만나면 종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    # 몸과 만나면 종료
    if (nx, ny) in snake:
        break

    # 사과를 먹으면 몸이 길어짐
    if graph[nx][ny] == 1:
        snake.appendleft((nx, ny))
        # 사과 치우기
        graph[nx][ny] = 0
    else:
        snake.appendleft((nx, ny))
        snake.pop()

print(time)
