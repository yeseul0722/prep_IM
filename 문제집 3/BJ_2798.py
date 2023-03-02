import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in cards:
    total = 0
    for j in cards:
        if i == j:
            continue
        for k in cards:
            if i == k or j == k:
                continue
            total = i + j + k
            if total > M:
                continue
            if total > result:
                result = total

print(result)