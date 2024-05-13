n = int(input())
num = list(map(int,input().split()))
min_ = float("inf")  
for i in range(len(num)):
    for j in range(len(num)):
        if abs(num[j]-num[i])!=0 and abs(num[j]-num[i]) < min_:
            min_ = abs(num[j]-num[i])
print(min_)