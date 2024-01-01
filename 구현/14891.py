import sys
from collections import deque
input = sys.stdin.readline

arr = [0]
for _ in range(4):
    arr.append(deque(list(map(int, input().rstrip()))))
k = int(input())

for _ in range(k):
    history = [0]
    for i in range(1, 4):
        history.append(arr[i][2] == arr[i+1][6])
    n, m = map(int, input().split())
    r, l = -m, -m
    if m == 1:
        arr[n].appendleft(arr[n].pop())
    else:
        arr[n].append(arr[n].popleft())
    for i in range(n+1, 5):
        if history[i-1]:
            break
        if r == 1:
            arr[i].appendleft(arr[i].pop())
        else:
            arr[i].append(arr[i].popleft())
        r *= -1
    for i in range(n-1, 0, -1):
        if history[i]:
            break
        if l == 1:
            arr[i].appendleft(arr[i].pop())
        else:
            arr[i].append(arr[i].popleft())
        l *= -1
result = 0
for i in range(1, 5):
    if arr[i][0] == 1:
        result += 2**(i-1)
print(result)
