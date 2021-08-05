#모험가 길드(틀림ㅠㅠ)

# #공포도가 X 공포도가 X인 모험가는 반드시 X명 이상
#
# N = 5
# man = [4,3,1,2,2]
# max_num =0
#
#
# #1,2,3 #2,2
#
# #안에 있는 값을 sorting 하고
#
# man.sort(reverse=True)
# max_num = man[0]
# second_max_num = 0
#
# for i in range(N):
#     if(man[i] != max_num):
#         second_max_num = man[i]
#         break
#
# num = list(0 for i in range(N))
#
# g = N // max_num
# extra_g = N % max_num
# extra_g = extra_g // second_max_num
#
# g = g + extra_g
#
# print(g)


#답안지
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 스룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 포함된 모험가의 수
    if count >= i : #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)