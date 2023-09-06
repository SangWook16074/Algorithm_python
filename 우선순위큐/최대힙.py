import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -m)