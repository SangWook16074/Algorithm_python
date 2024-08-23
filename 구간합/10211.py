import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    psum = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        psum[i] = psum[i - 1] + arr[i - 1]
    ans = -1000 * 1000
    for i in range(1, n+1):
        for j in range(i, n+1):
            ans = max(ans, psum[j] - psum[i - 1])
    print(ans)
