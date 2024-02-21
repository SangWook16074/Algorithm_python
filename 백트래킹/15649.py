import sys
input = sys.stdin.readline


def back():
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            back()
            result.pop()


n, m = map(int, input().split())
result = []
back()
