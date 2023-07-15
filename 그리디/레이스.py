# 문제
# 세준이는 세준항공으로 돈을 무지막지하게 번 뒤, 레이스 대회를 개최했다. 레이스 트랙은 길이가 N인 직선이다.

# 세준이는 심판 M명을 적절한 곳에 배치시키려고 한다. 심판은 아무 곳에나 배치시킬 수 있지 않다. 
# 심판은 미리 정해진 K개의 곳에만 위치할 수 있다.

# 세준이는 심판을 배치할 때, 가장 가까운 두 심판의 거리를 최대로 하려고 한다.

# 심판을 어디에 배치시켜야 할지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, M, K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, M은 K보다 작거나 같은 자연수이다. 
# 또, K는 2보다 크거나 같고, 50보다 작거나 같다. 둘째 줄에 심판이 있을 수 있는 K개의 위치가 주어진다. 
# K개의 위치는 N보다 작거나 같은 자연수 또는 0이며, 오름차순으로 주어진다.

# 출력
# 첫째 줄에 심판을 어떻게 배치시켜야 가장 가까운 심판의 거리가 최대가 될 것인지 출력한다. 
# 출력할 때는 예제와 같이 심판을 세울 곳에는 1을, 세우지 않을 곳에는 0을 출력한다. 
# 만약 정답이 여러개일 경우에는 사전순으로 가장 늦는 것을 출력한다.

# 예제 입력 1 
# 11 3 4
# 0 5 10 11
# 예제 출력 1 
# 1110
# 예제 입력 2 
# 11 2 4
# 0 5 10 11
# 예제 출력 2 
# 1001
# 예제 입력 3 
# 11 4 4
# 0 5 10 11
# 예제 출력 3 
# 1111
# 예제 입력 4 
# 1000 5 10
# 6 9 33 59 100 341 431 444 565 857
# 예제 출력 4 
# 1000010111

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
position = list(map(int, input().split()))

