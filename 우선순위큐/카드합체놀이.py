import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
h = []
for card in list(map(int, input().split())):
    heapq.heappush(h, card)

for _ in range(m):
    # 카드 선택
    total = heapq.heappop(h) + heapq.heappop(h)
    heapq.heappush(h, total)
    heapq.heappush(h, total)
print(sum(h))