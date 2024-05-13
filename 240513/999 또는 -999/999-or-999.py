num = list(map(int,input().split()))
max_, min_ = num[0], num[0]
for i in num:
    if i != 999 and i != -999:
        if max_ < i:
            max_ = i
        if min_ > i:
            min_ = i
    else:
        break
print(f'{max_} {min_}')