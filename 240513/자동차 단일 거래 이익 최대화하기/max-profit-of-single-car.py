n = int(input())
cost = list(map(int,input().split()))
max_ = 0
for i in range(len(cost)):
    for j in range(i,len(cost)):
        if j-i > max_:
            max_ = j-i
print(max_)