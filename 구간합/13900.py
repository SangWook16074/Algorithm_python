import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
psum = [0]
total = 0
for num in nums:
    total += num
    psum.append(total)
result = 0
for i in range(1, n+1):
    result += nums[i-1]*(psum[n]-psum[i])
print(result)
