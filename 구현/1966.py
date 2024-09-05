import sys
from collections import deque
input = sys.stdin.readline

def findOverPerioty(idx, arr):
    if not arr:
        return False

    for a in arr:
        if a[0] > idx:
            return True
    return False

for _ in range(int(input())):
    printQueue = deque()
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        printQueue.append([arr[i], i])
    
    cnt = 1
    while printQueue:
        curr = printQueue.popleft()
        if findOverPerioty(curr[0], printQueue):
            printQueue.append(curr)
            continue
        
        if curr[1] == m:
            print(cnt)
            break
        
        cnt += 1