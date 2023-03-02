import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
i = 1

while N > 1:
    N = N - (6 * i)
    cnt += 1
    i += 1
print(cnt)
