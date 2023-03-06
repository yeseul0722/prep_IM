C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 0

seats = [[0] * C for _ in range(R)]
nowX = 0
nowY = R - 1

for i in range(1, (C * R) + 1):
    seats[nowY][nowX] = i
    if seats[nowY][nowX] == K:
        print(nowX + 1, R - nowY)
        break
    if 0 <= nowY + dy[d] < R and 0 <= nowX + dx[d] < C and seats[nowY + dy[d]][nowX + dx[d]] == 0:
        nowY = nowY + dy[d]
        nowX = nowX + dx[d]
    else:
        if d == 3:
            d = 0
        else:
            d += 1
        nowY = nowY + dy[d]
        nowX = nowX + dx[d]
