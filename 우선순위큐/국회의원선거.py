import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())
dasom = int(input())
if n == 1:
    print(0)
else:
    for _ in range(n-1):
        heapq.heappush(h, -int(input()))
    result = 0
    while True:
        maximum = -heapq.heappop(h)
        if maximum < dasom:
            break
        else:
            maximum -= 1
            result += 1
            dasom += 1
            heapq.heappush(h, -maximum)
    print(result)