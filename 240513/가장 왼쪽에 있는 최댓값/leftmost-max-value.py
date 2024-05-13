n = int(input())
num = list(map(int,input().split()))

while True:
    max_ = max(num)
    max_idx = num.index(max_)
    if max_idx != 0:
        print(max_idx + 1, end=" ")
        num = num[:max_idx]
    else:
        print(1, end=" ")
        break