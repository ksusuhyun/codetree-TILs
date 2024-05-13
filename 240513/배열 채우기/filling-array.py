num = list(map(int,input().split()))
l = []
for i in num:
    if i != 0:
        l.append(i)
    else:
        break
for j in l[::-1]:
    print(j, end=" ")