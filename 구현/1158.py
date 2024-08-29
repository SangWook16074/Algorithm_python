import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
ans = []
idx = 0
for _ in range(n):
    idx += k - 1
    if idx >= len(arr):
        idx %= len(arr)
    ans.append(arr.pop(idx))

print("<", ", ".join(str(i) for i in ans),">", sep="")
