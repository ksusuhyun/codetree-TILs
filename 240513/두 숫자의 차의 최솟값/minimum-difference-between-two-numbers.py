n = int(input())
num = list(map(int,input().split()))
min_ = float("inf")  
for i in range(len(num)):
    for j in range(len(num)):
        if j-i!=0 and j-i < min_:
            min_ = j-i
print(min_)