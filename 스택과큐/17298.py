import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0 for _ in range(n)]
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

while stack:
    result[stack.pop()] = -1

print(*result)
