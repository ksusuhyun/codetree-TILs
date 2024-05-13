a, b = map(int,input().split())
l = [0, a, b]
for i in range(3,11):
    l.append(int((l[i-2]+l[i-1])%10))
for i in l[1:]:
    print(i,end=" ")