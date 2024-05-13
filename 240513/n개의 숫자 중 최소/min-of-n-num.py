n = int(input())
num = list(map(int,input().split()))
min_ = num[0]
for i in num[1:]:
    if i < min_:
        min_ = i
print(f'{min_} {num.count(min_)}')