import sys
input = sys.stdin.readline

total = 0
arr = [int(input()) for _ in range(10)]

for i in range(10):
    if abs(total + arr[i] - 100) <= abs(total - 100):
        total += arr[i]
    else:
        break
print(total)