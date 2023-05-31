# 문제
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

# 출력
# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

# 예제 입력 1 
# 5
# 6
# 8
# 10
# 12
# 100
# 예제 출력 1 
# 1
# 1
# 2
# 1
# 6

import sys

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    result = {}

    
    for i in range(2, n):
        if sieve[i]:           # i가 소수인 경우 
            result[i] = 0
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return result

t = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(t):
    arr.append(int(sys.stdin.readline().rstrip()))

for t in arr:
    primes = prime_list(max(arr))
     
    cnt = 0
    for prime in list(filter(lambda x : x <= t // 2, list(primes.keys()))):
        if t - prime in list(filter(lambda x : x >= t//2 and x <= t, list(primes.keys()))):
            cnt += 1

            
    print(cnt)
