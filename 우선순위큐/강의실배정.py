import sys
import heapq
input = sys.stdin.readline

lectures = []
n = int(input())
for _ in range(n):
    lectures.append(list(map(int, input().split())))
lectures = sorted(lectures, key=lambda x : (x[0], x[1]))
h = []
heapq.heappush(h, lectures[0][1])
for i in range(1, n):
    if lectures[i][0] < h[0]:
        heapq.heappush(h, lectures[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, lectures[i][1])
print(len(h))

