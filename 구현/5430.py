import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    command = list(input().rstrip())
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    q = deque(arr) if n != 0 else []
    isError = False
    rev = 0
    for c in command:
        if c == "R":
            rev += 1
        else:
            if len(q) == 0:
                print("error")
                isError = True
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if not isError:
        if rev % 2 == 0:
            print("["+",".join(q)+"]")
        else:
            q = deque(reversed(q))
            print("["+",".join(q)+"]")
