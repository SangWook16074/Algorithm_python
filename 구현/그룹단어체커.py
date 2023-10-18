import sys
input = sys.stdin.readline

def check(word):
    check = [word[0]]
    current = word[0]
    for i in range(1, len(word)):
        if word[i] != current and word[i] not in check:
            check.append(word[i])
            current = word[i]
        elif word[i] != current and word[i] in check:
            return False
    return True

n = int(input())
result = 0
for _ in range(n):
    word = input()
    if check(word):
        result += 1
print(result)