n = int(input())
num = list(map(int,input().split()))
min_ = float("inf")  
for i in range(len(num)):
    for j in range(len(num)):
        if abs(j-i) < min_:
            min_ = abs(j-i)
print(min_)