import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
prices = list(map(int, input().split()))
price = 10000
result = 0
for i in range(n-1):
    price = min(price, prices[i])
    result += price * length[i]
print(result)
