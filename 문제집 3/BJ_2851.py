

sum_ = 0
for T in range(10):
    num = int(input())
    sum_ += num
    if sum_ >= 100:
        if sum_ - 100 > 100 - (sum_ - num):
            sum_ = sum_ - num
        break

print(sum_)

