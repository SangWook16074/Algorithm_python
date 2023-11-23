import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0 for _ in range(n)]
for i in range(1, n+1):
    kevin = [0 for _ in range(n+1)]
    q = deque()
    q.append(i)
    while q:
        p = q.popleft()
        for f in graph[p]:
            if f == i:
                continue
            
            if kevin[f] == 0:
                kevin[f] = kevin[p]+1
                q.append(f)
    result[i-1] += sum(kevin)

print(result.index(min(result))+1)