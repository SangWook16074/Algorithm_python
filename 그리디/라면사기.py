# 문제
# 라면매니아 교준이네 집 주변에는 N개의 라면 공장이 있다. 
# 각 공장은 1번부터 N번까지 차례대로 번호가 부여되어 있다. 
# 교준이는 i번 공장에서 정확하게 Ai개의 라면을 구매하고자 한다(1 ≤ i ≤ N).

# 교준이는 아래의 세 가지 방법으로 라면을 구매할 수 있다.

# i번 공장에서 라면을 하나 구매한다(1 ≤ i ≤ N). 이 경우 비용은 3원이 든다.
# i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-1). 이 경우 비용은 5원이 든다.
# i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-2). 이 경우 비용은 7원이 든다.
# 최소의 비용으로 라면을 구매하고자 할 때, 교준이가 필요한 금액을 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 라면 공장의 개수를 의미하는 자연수 N가 주어진다.

# 두번째 줄에 N개의 정수 A1, ···, AN가 사이에 공백을 두고 주어진다.

# 출력
# 첫 번째 줄에 교준이가 필요한 최소 금액을 출력한다.

# 제한
# 모든 입력 데이터는 다음 조건을 만족한다.

# 3 ≤ N ≤ 104
# 0 ≤ Ai ≤ 104 (1 ≤ i ≤ N)
# 예제 입력 1 
# 3
# 1 0 1
# 예제 출력 1 
# 6
# 예제 입력 2 
# 5
# 1 1 1 0 2
# 예제 출력 2 
# 13

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
stack = 0
min_arr = 105

for i in range(n):
    if arr[i] > 0:
        result += arr[i]*3
        stack += 1
        min_arr = min(arr[i], min_arr)

    elif stack == 3 or arr[i] == 0:
        result -= min_arr*(stack-1)
        stack = 0

    elif arr[i] == 0:
        stack = 0
  
print(result)


# 라면을 하나만 구매하면 3원이 필요함
# 라면을 두개 연속의 공장에서 사면 1원 절약 가능
# 라면을 세개 연속의 공장에서 사면 2원 절약 가능