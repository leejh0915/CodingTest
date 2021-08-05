#그리디 알고리즘 1

#N = 1260 이 거스름 돈일때의 돈 계산

# N = 12600
#
# r500 = 0
# r100 = 0
# r50 = 0
# r10 = 0
#
# if N>=500 :
#     r500 = N//500
#     N = N%500
# if N>=100 :
#     r100 =N//100
#     N = N%100
# if N>=50 :
#     r50 = N//50
#     N = N%50
# if N>= 10 :
#     r10 = N//10
#     N = N%10
#
# print(r500)
# print(r100)
# print(r50)
# print(r10)

# n = 1260
# count = 0
#
# # 큰 단위의 화폐부터 차례대로 확인하기
# coin_types = [500, 100, 50, 10]
#
# for coin in coin_types:
#     count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin
#
# print(count)

# #큰 수의 법칙 내가 푼 것
#
# M = 8
# K = 3
#
# #num = [3,4,3,4,3]
# num = [2,4,5,4,6]
# total = 0
#
# num.sort(key=None, reverse=True)
#
# max_num = num[0]
#
# print(num)
# count =0
#
# for i in num:
#     if count == 0:
#         total += i*K*(M//K)
#         count += K * (M//K)
#     else:
#         total += i*(M%K)
#         count += M%K
#
#     if count == M :
#         break
#
# print(total)



# # N, M, K 를 공백으로 구분하여 입력받기
# n,m,k =map(int, input().split()) #이건 무엇인고?
#
# #map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
# #input
#
# #input().split은 입력 받은 숫자를 나누는 역활을 한다
#
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
#
# data.sort() # 입력받은 수들 정렬하기
# first = data[n-1] #가장 큰 수
# second =data[n-2] #두 번째로 큰 수
#
# result = 0
#
# while True:
#     for i in range(k): #가장 큰 수를 K번 더하기
#         if m == 0:
#             break
#         result += first
#         m -= 1 #더할 때마다 1씩 빼기
#     if m == 0: #m이 0이라면 반복문 탈출
#         break
#     result += second #두 번쨰로 큰 수를 한 번 더하기
#     m -= 1 #더할 때마다 1씩 빼기
#
# print(result)

# card = [[1,2,3],[5,4,6],[9,7,8]]
#
# N =3     #행의 개수
#
# card_rows = list(range(N))
# max_value = 0
#
# for i in range(N) :
#     card[i].sort()
#     card_rows[i] = card[i][0]
#
# print(card_rows)
#
# for i in range(N):
#     if(max_value < card_rows[i]):
#         max_value = card_rows[i]
#
# print(max_value)

# #N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
#
# result = 0
#
# #한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     #현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     #'가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result)

# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
#
# result =0
# # 한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result) #최종 답안 출력

# n, k = map(int, input().split)
#
# cnt =0
#
# while n != 1:
#     if(n%k == 0):
#         n = n//k
#     else:
#         n = n-1
#     cnt+=1
#
# print(cnt)

n, k =map(int, input().split())
result =0

while True:
    #(N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target =(n // k)*k
    result += (n - target)
    n = target

    #N이 K보다 작을 때(더 이상 나눌 수 없을 때)반복문 탈출
    if n < k:
        break

    #K로 나누기
    result += 1
    n //=k
    print(n)


# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)