import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

low, high = 0, 0
ans = n + 1
total = arr[0]
while low <= high and high < n:
    if total < s:
        high += 1
        if high == n:
            continue
        total += arr[high]
    else:
        ans = min(ans, high - low + 1)
        total -= arr[low]
        low += 1
if ans == n + 1: ans = 0
print(ans)
