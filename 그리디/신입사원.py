import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr = sorted(arr, key= lambda x : (x[0], x[1]))
    result = 1
    first = arr[0]
    for i in range(1, n):
        if arr[i][0] < first[0] or arr[i][1] < first[1]:
            result += 1
            first = arr[i]
    print(result)


