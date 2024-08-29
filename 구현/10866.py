from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
deque = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "push_front":
        deque.appendleft(int(command[1]))
    elif command[0] == "push_back":
        deque.append(int(command[1]))
    elif command[0] == "pop_front":
        print(deque.popleft() if len(deque) != 0 else -1)
    elif command[0] == "pop_back":
        print(deque.pop() if len(deque) != 0 else -1)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(1 if len(deque) == 0 else 0)
    elif command[0] == "front":
        print(deque[0] if len(deque) != 0 else -1)
    elif command[0] == "back":
        print(deque[-1] if len(deque) != 0 else -1)