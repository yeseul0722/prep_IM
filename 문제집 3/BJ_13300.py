# 남학생 리스트, 여학생 리스트를 따로 만들어 정보에 따라 담기
# 포문으로 6학년까지 돌면서 방에 넣어주기


import sys
import math
input = sys.stdin.readline

boys = []
girls = []
result = 0
N, K = map(int, input().split())
for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        girls.append(Y)
    else:
        boys.append(Y)


for j in range(1, 7):
    cnt_girls = 0
    cnt_boys = 0
    for year in girls:
        if j == year:
            cnt_girls += 1
    result += math.ceil(cnt_girls / K)
    for year in boys:
        if j == year:
            cnt_boys += 1
    result += math.ceil(cnt_boys / K)

print(result)