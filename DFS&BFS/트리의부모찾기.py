import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit[1] = True
for i in range(1, n+1):
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        for n in tree[now]:
            if not visit[n]:
                visit[n] = True
                result[n] = now
                q.append(n)
for i in range(2, len(result)):
    print(result[i])