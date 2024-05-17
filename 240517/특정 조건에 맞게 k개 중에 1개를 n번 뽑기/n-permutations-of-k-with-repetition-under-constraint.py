k, n = map(int,input().split())

res = []
def choice(curr_num):
    if curr_num >= n :
        print(*res)
        return

    for i in range(1,k+1):
        if (len(res) < 2) or (res[-2] != i and res[-1] != i):
            res.append(i)
            choice(curr_num+1)
            res.pop()

choice(0)