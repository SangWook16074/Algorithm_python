import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    result = False
    n = int(input())
    start = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(n)]
    visit = [False for _ in range(n)]
    end = list(map(int, input().split()))
    q = deque()
    q.append((start[0], start[1]))
    while q:
        x, y = q.popleft()
        if abs(x-end[0])+abs(y-end[1]) <= 1000:
            result = True
        else:
            for i in range(n):
                if visit[i]:
                    continue

                if abs(x-graph[i][0]) + abs(y-graph[i][1]) > 1000:
                    continue

                visit[i] = True
                q.append((graph[i][0], graph[i][1]))
    if result:
        print("happy")
    else:
        print("sad")