import sys
input = sys.stdin.readline

remainder_list = []
for _ in range(10):
    num = int(input())
    remainder = num % 42
    if not remainder in remainder_list:
        remainder_list.append(remainder)

print(len(remainder_list))