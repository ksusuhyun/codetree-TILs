a, b = map(int,input().split())
n = [0,a,b]
for i in range(3,11):
    n.append(2*n[i-2] + n[i-1])
for j in n:
    print(j, end=" ")