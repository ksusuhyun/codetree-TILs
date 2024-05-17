n = int(input())
visit = [False]*(n+1)
res = []

def choice(curr_num):
    if curr_num > n:
        print(*res)
        return
    
    for i in range(1,n+1):
        if visit[i] == True:
            continue

        res.append(i)
        visit[i] = True
        choice(curr_num+1)
        res.pop()
        visit[i] = False

choice(1)