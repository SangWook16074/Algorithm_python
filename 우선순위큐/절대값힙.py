import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(h, (abs(num), num))
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])