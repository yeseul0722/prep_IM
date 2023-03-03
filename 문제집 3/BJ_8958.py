import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    string = list(input())
    result = 0
    point = 0
    for i in range(len(string)):
        if string[i] == 'O':
            if string[i] == string[i - 1]:
                point += 1
                result += point
            else:
                point = 1
                result += point

        else:
            point = 0

    print(result)