import sys
input = sys.stdin.readline

picture = []
score = []
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
for i in range(m):
    if arr[i] in picture:
        for j in range(len(picture)):
            if picture[j] == arr[i]:
                score[j] += 1
    else:
        if len(picture) == n:
            for j in range(n):
                if score[j] == min(score):
                    del picture[j]
                    del score[j]
                    break
        picture.append(arr[i])
        score.append(1)
picture.sort()
print(" ".join(map(str, picture)))


