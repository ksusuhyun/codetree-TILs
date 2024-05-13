L = []
for i in range(2):
    a = list(map(int,input().split()))
    L.append(a)

s = 0
for i in L:
    print(round(sum(i)/4,1),end=' ')
    s += sum(i)
print()
for i in range(4):
    sum = 0
    for j in range(2):
        sum += L[j][i]
    print(round(sum/2,1), end=' ')
print()
print(round(s/8,1))