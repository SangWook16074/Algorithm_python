import sys
input = sys.stdin.readline

n = int(input())
arr = []
total = 0
for _ in range(n):
    x, a = map(int, input().split())
    total += a
    arr.append([x, a])
arr = sorted(arr, key= lambda x : x[0])
cnt = 0
for i in range(n):
    cnt += arr[i][1]
    if cnt >= total / 2:
        print(arr[i][0])
        exit()
