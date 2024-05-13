n = int(input())
num = [1,n]
i = 0
while True:
    if num[i] + num[i+1] < 100:
        num.append(num[i] + num[i+1])
        i += 1
    else:
        num.append(num[i] + num[i+1])
        break
for i in num:
    print(i,end=" ")