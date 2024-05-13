num = [
    list(map(int,input().split()))
    for i in range(4)
]
sum_ = 0
for i in range(4):
    for j in range(i,4):
        sum_ += num[j][i]
print(sum_)