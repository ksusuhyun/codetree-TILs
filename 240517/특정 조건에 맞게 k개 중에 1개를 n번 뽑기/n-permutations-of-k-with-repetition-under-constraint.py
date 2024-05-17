k, n = map(int,input().split())

res = []
def choice(curr_num):
    if curr_num >= n :
        print(*res)
        return

    for i in range(1,k+1):
        # 함수 호출을 안 하는 경우
        # => 연속해서 같은 숫자가 3개가 되는 경우
        if curr_num >= 2 and res[-2] == i and res[-1] == i:
            continue
        res.append(i)
        choice(curr_num+1)
        res.pop()

choice(0)