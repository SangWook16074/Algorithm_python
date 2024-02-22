import sys
input = sys.stdin.readline

moum = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
arr = sorted(input().split())
result = []


def check(result):
    cnt = 0
    for m in moum:
        if m in result:
            cnt += 1

    if 1 <= cnt <= l-2:
        return True
    else:
        return False


def back(idx):
    if len(result) == l and check(result):

        print("".join(result))
        return

    if len(result) == l and not check(result):
        return

    for i in range(idx, c):
        if arr[i] not in result:
            result.append(arr[i])
            back(i)
            result.pop()


back(0)
