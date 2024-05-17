n, m = map(int,input().split())

num = [i for i in range(1,n+1)]

res = []
def choice(curr_num,cnt):
    if curr_num > n:
        if cnt == m :
            for i in range(len(res)):
                if res[i] == 0:
                    print(num[i], end=" ")
            print()
        return
    
    res.append(0)
    choice(curr_num+1,cnt+1)
    res.pop()

    res.append(1)
    choice(curr_num+1,cnt)
    res.pop()

choice(1,0)