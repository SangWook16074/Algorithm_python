# 입체기동장치 생산공장에서는 거인들을 물리치기 위한 기계가 생산되고 있습니다.

# 이 공장을 운영하는 에렌은 입체기동장치(1~100)의 식별번호(1~100)와 가스 보유량(0~10000)을 같이 관리하려고 합니다.

# 하지만, 식별번호를 정렬할 때 가스 보유량이 뒤죽박죽 되어 버려 골머리를 앓고 있습니다.

# 에렌을 남몰래 좋아하고 있던 미카사는 에렌이 스트레스성 탈모로 잔머리가 모두 빠지기 전에 이 문제를 해결해주려 합니다.

# 미카사가 에렌의 스트레스성 탈모를 막을 수 있도록 프로그램을 작성해세요.

# 식별번호가 한번 정해지면 그 입체기동장치의 가스 보유량은 정렬되더라도 변하지 않아야 합니다.

# 입력
# 첫째 줄에 입체기동장치의 갯수 n이 입력된다. (1 <= n <= 100)

# 둘째 줄부터 n+1째 줄까지 각 줄에 입체기동장치의 식별번호 a와 가스 보유량 b가 주어진다.

# a는 중복 될 수 없지만 b는 중복될 수 있다. (1 <= a <= 100), (0 <= b <= 10,000)

# 출력
# 첫째 줄부터 n번째 줄까지 각 줄에 식별번호를 오름차순으로 정렬해 가스 보유량과 같이 출력한다.

# 풀이

# couple = []
# n = input()

# for i in range(int(n)):
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     couple.append([a, b])

# for i in range(len(couple)-1):
#     for j in range(len(couple)-1):
#         a = couple[j][0]
#         b = couple[j+1][0]
#         if (a < b):
#             pass
#         else:
#             tmp = couple[j+1]
#             couple[j+1] = couple[j]
#             couple[j] = tmp

# for i in range(len(couple)):
#     print(couple[i][0], couple[i][1])



# 프로그래밍 문제를 풀다 보면 뒤죽박죽인 N개의 데이터를 숫자의 크기 순으로 0 ~ N-1까지의 숫자로 재정렬 해야되는 경우가 종종 있다.

# 예를 들어 N=5 이고,

# 50 23 54 24 123

# 이라는 데이터가 있다면,

# 2 0 3 1 4

# 가 된다.

# 데이터를 재정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 데이터의 개수 N이 입력된다. ( 1 <= N <= 50,000)

# 둘째 줄에 공백으로 분리되어 N개의 서로 다른 데이터가 입력된다. (값의 범위:0~500,000)

# 출력
# N개의 데이터를 0 ~ N-1로 재정렬하여 출력하라.

# n = int(input())

# th = []
# arr = []
# for i in range(n):
#     num = int(input())
#     arr.append(num)
#     th.append(num)

# print(th)
# arr.sort()
# print(arr)
# for i in range(n):
#     tmp = arr[i]
#     for j in range(n):
#         if(th[j] != tmp):
#             pass
#         else:
#             th[j] = i

# print(*th)



# for i in range(len(arr)):
#     if(arr2[i] != arr[i]):
#         pass
#     else:
#         arr2[i] = i

# print(*arr2)
# import sys
# n, m = map(int, sys.stdin.readline().split())




    
    


# if n % i == 0:
#     arr.append(i)

# print(sum(arr))






import sys
n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
cnt = 1
arr = []
arr2 = []
if n == 1:
    print(1)
else:
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            cnt += 1
        else:
            arr.append(cnt)
            cnt = 1
        
        if i == n-2:
            arr.append(cnt)



        
# 99 3 4 2
# 2 99 1 2
# 2 99 3 2
print(arr)


## 관건
## 오른쪽이든 왼쪽이든 많은 방향의 불상이 주가 되어야 함.

## 결론 방향이 많이 나오는 불쌍이 시작되는 부분부터 끝나는 부분까지 색칠하면 됨.
## 단, 중간에 낑긴 경우에 잘린 토막이 낑긴 토막보다 짧으면 안칠하는게 이득임.
## 
## 1 1 1 1 2 2 1 2 2 2 2 2
## 
## 어떤 경우에
## 연속된 불상 말고 절대값이 유리한거지??
## 
## 100
## 1 1 1 1 ... 2 1 1 1 1 = 99
## 1 1 1 1 ... 1 2 1 1 1 = 99
## 1 1 1 1 ... 1 1 2 1 1 = 99
## 1 1 1 1 ... 1 1 1 2 1 = 98
## 1 1 1 1 ... 1 1 2 1 2 = 99


## 1 1 1 1 ... 1 1 2 2 1 = 98
## 1 1 1 1 ... 1 2 2 1 1 = 98
## 1 1 1 1 ... 2 2 1 1 1 = 98
## 1 1 1 1 ... 1 1 2 1 1 = 99
## 1 1 1 1 ... 1 1 2 1 1 = 99
