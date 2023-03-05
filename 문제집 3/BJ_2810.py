# S = 일반 좌석 L = 커플석

N = int(input())
seats = list(input())

cnt = 0
for i in seats:
    if i == "S":
        cnt += 1
    if i == "L":
        cnt += 0.5

if cnt < N:
    cnt += 1

print(int(cnt))