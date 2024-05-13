a, b = map(int,input().split())
cnt = {}
while a > 1:
    if a % b in cnt:
        cnt[a % b] += 1
    else :
        cnt[a % b] = 1
    a = a // b
sum = 0
for i in cnt.values():
    sum += i**2
print(sum)