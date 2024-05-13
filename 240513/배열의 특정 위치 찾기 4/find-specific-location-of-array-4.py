num = list(map(int,input().split()))
sum = 0
cnt = 0
for i in num:
    if i != 0 and i % 2 == 0:
        sum += i
        cnt += 1
    elif i == 0:
        break
print(f'{cnt} {sum}')