n = int(input())
jenga = [int(input()) for _ in range(n)]
s1,e1 = map(int,input().split())
s2,e2 = map(int,input().split())

def take_out(jenga,s,e):
    for i in range(s-1,e):
        jenga[i] = 0
    temp = []
    for j in jenga:
        if j != 0:
            temp.append(j)
    jenga = temp
    return jenga

jenga = take_out(jenga,s1,e1)
res = take_out(jenga,s2,e2)
print(len(res))
for j in res:
    print(j)