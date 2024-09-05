import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

print(int(round(sum(arr) / n, 0)))
print(arr[n // 2])

most_value = sorted(list(map(list, Counter(arr).most_common(n))), key= lambda x : (-x[1], x[0]))
if len(most_value) > 1 and most_value[0][1] == most_value[1][1]:
    print(most_value[1][0])
else:
    print(most_value[0][0])
print(int(max(arr) - min(arr)))