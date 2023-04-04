# 문제
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

# 예제 입력 1 
# ZZZZZ 36
# 예제 출력 1 
# 60466175
# 11001 2
#     2**0
# import sys

# alphabet = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# n, b = sys.stdin.readline().split()
# n = list(n)
# b = int(b)
# n.reverse()

# result = 0
# for i in range(len(n)):
#     tmp = alphabet.index(n[i])*(b**i)
#     result += tmp

# print(result)

import sys

n, b = sys.stdin.readline().split()
b = int(b)
print(int(n, b))


