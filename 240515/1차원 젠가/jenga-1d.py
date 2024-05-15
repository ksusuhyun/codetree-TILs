n = int(input())
jenga = [int(input()) for _ in range(n)]

def take_out(jenga,s,e):
    for i in range(s-1,e):
        jenga[i] = 0
    temp = []
    for j in jenga:
        if j != 0:
            temp.append(j)
    jenga = temp
    return jenga


for _ in range(2):
    s, e = map(int,input().split())
    jenga = take_out(jenga,s,e)

print(len(jenga))
for j in jenga:
    print(j)