import sys
input = sys.stdin.readline

N = int(input())
students = []
order = list(map(int, input().split()))

student = 1
for i in order:
    if i == 0:
        students.append(student)
    if i > 0:
        students.insert(-i, student)  # insert 함수 사용시 -1 위치에 추가하면
    student += 1                      # 마지막 요소의 한칸 앞에 위치시킴

print(*students)
