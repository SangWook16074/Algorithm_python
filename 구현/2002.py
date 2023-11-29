import sys
input = sys.stdin.readline

n = int(input())
start = [input().rstrip() for _ in range(n)]
end = [input().rstrip() for _ in range(n)]
idx = 0
result = 0
for e in end:
    current = start[idx]
    if e != current:
        result += 1
        start.remove(e)
    else:
        idx += 1
print(result)