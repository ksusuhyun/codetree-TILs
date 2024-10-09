n = int(input())
num = list(map(int, input().split()))

for i in range(len(num)-1):
    for j in range(len(num)-1):
        if num[j] > num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp

print(*num)