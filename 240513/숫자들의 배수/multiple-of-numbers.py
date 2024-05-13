n = int(input())
l = []
i = 1
cnt = 0
while cnt < 2:
    if n*i % 5 != 0:
        l.append(n*i)
        i += 1
    else:
        l.append(n*i)
        i += 1
        cnt += 1
for i in l:
    print(i,end=" ")