

L = int(input())
cake = [0] * (L + 1)
N = int(input())
most_a = 0
expect = 0
most_b = 0
result = 0
for i in range(1, N + 1):
    P, K = map(int, input().split())
    if K - P > most_a:
        most_a = K - P
        expect = i
    cnt = 0
    for j in range(P, K + 1):
        if cake[j] == 0:
            cake[j] = i
            cnt += 1
        if cnt > most_b:
            most_b = cnt
            result = i
print(expect, result)

