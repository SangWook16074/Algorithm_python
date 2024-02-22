import sys
input = sys.stdin.readline

n = int(input())
cols = [0 for _ in range(n)]
result = 0


def check(row):
    for before in range(row):
        if (cols[before] == cols[row]) or (abs(cols[before] - cols[row]) == abs(before - row)):
            return False
    return True


def back(row):
    global result
    if row == n:
        result += 1
    else:
        for i in range(n):
            cols[row] = i
            if check(row):
                back(row+1)


back(0)
print(result)
