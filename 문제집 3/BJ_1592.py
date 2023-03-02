import sys
input = sys.stdin.readline

def play(number, length):
    count = 0
    start = 0                               # 무조건 1번 부터 시작이라 start = 0
    now = people[start]                     # 현재값 지정

    while now != number:
        if now % 2 == 0:
            start = (start + length) % N    # 원이니깐 범위를 벗어나면 안되니 나머지값 활용

        else:
            start = (start - length) % N

        people[start] += 1
        count += 1
        now = people[start]

    return count



N, M, L = map(int, input().split())
people = [0] * N
people[0] = 1


print(play(M, L))


