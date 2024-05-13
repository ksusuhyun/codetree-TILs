n = int(input())
p = 0
for i in range(n):
    score = list(map(int,input().split()))
    mean = sum(score)/len(score)
    if mean >= 60:
        print('pass')
        p += 1
    else:
        print('fail')
print(p)