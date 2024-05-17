k, n = map(int,input().split())

res = []
def choice(curr_num):
    if curr_num >= n :
        print(*res)
        return

    for i in range(1,k+1):
        if res.count(i) < 3:
            res.append(i)
            choice(curr_num+1)
            res.pop()

choice(0)