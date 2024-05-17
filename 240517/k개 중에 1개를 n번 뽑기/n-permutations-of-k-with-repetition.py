# N자리 k진수 만들기

# 현재 위치보다 앞에는 1~k 중 하나가 이미 선택되었고
# 현재 위치에서 1~k 중 하나를 선택한 다음
# 다음 위치가 선택하도록 함수를 호출한다

k, n = map(int,input().split())

res = []
def choice(curr_num):
    if curr_num >= n:
        for num in res:
            print(num, end=" ")
        print()
        return
    for i in range(1,k+1):
        res.append(i)
        choice(curr_num+1)
        res.pop()

choice(0)