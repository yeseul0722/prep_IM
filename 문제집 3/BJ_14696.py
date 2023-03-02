# 별: 4, 동그라미 : 3, 네모: 2, 세모: 1

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A, *card_A = map(int, input().split())
    B, *card_B = map(int, input().split())

    if card_A.count(4) > card_B.count(4):
        print('A')
    elif card_A.count(4) < card_B.count(4):
        print('B')
    elif card_A.count(3) > card_B.count(3):
        print('A')
    elif card_A.count(3) < card_B.count(3):
        print('B')
    elif card_A.count(2) > card_B.count(2):
        print('A')
    elif card_A.count(2) < card_B.count(2):
        print('B')
    elif card_A.count(1) > card_B.count(1):
        print('A')
    elif card_A.count(1) < card_B.count(1):
        print('B')
    else:
        print('D')