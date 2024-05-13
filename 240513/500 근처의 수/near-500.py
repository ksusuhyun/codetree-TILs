num = list(map(int,input().split()))
max_, min_ = num[0], num[0]
for i in num:
    if i<500 and max_ < i:
        max_ = i
    if i>500 and min_ > i:
        min_ = i
print(f'{max_} {min_}')