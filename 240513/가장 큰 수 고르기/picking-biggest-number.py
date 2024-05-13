num = list(map(int,input().split()))
max_ = 0
for i in num:
    if i > max_:
        max_ = i
print(max_)