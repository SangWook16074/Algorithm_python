import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
psum = [0]
pre_sum = 0
for t in temp:
    pre_sum += t
    psum.append(pre_sum)

result = []
for i in range(n-k+1):
    total = psum[i+k] - psum[i]
    result.append(total)
print(max(result))
