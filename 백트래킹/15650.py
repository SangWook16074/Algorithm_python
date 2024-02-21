import sys
input = sys.stdin.readline


def back(x):
    if len(result) == m:
        print(*result)
        return

    for i in range(x, n+1):
        if i not in result:
            result.append(i)
            back(i)
            result.pop()


n, m = map(int, input().split())
result = []
back(1)
