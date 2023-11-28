import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0]*w)
result = 0
while True:
    result += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    if not bridge:
        break
print(result)