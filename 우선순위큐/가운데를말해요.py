import sys
import heapq
input = sys.stdin.readline

down_h = []
up_h = []
n = int(input())
for _ in range(n):
    num = int(input())
    if len(down_h) == len(up_h):
        heapq.heappush(down_h, -num)
    else:
        heapq.heappush(up_h, num)
    if up_h and -down_h[0] > up_h[0]:
        down = -heapq.heappop(down_h)
        up = heapq.heappop(up_h)

        if down > up:
            heapq.heappush(up_h, down)
            heapq.heappush(down_h, -up)
    
    print(-down_h[0])

