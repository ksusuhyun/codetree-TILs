n = int(input())
cost = list(map(int,input().split()))
print(cost)
max_ = 0
for i in range(len(cost)):
    for j in range(i,len(cost)):
        if cost[j]-cost[i] > max_:
            max_ = cost[j]-cost[i]
print(max_)