n = int(input())
num = list(map(int,input().split()))
cnt = {}
for i in num:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
max_key = 0
for key, val in cnt.items():
    if val == 1 and key > max_key:
        max_key = key
print(max_key)