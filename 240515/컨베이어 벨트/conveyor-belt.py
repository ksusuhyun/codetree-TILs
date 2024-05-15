n, t = map(int,input().split())
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
num = num1+num2

def shift(num):
    temp = num[-1]
    for i in range(2*n-1,0,-1): # 내가 새롭게 정의할 위치
        num[i] = num[i-1]
    num[0] = temp
    return num

for k in range(t):
    num = shift(num)

for i in num[0:n]:
    print(i, end=" ")
print()
for j in num[n:2*n]:
    print(j, end=" ")