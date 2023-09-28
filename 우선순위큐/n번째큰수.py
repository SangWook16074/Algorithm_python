import heapq
import sys
input = sys.stdin.readline


n = int(input())
h = []
for _ in range(n):
    for a in list(map(int, input().split())):
        if len(h) < n:
            heapq.heappush(h, a)
        else:
            if h[0] < a:
                heapq.heappop(h)
                heapq.heappush(h, a)
print(h)
