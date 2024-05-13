m = [0,0,0,0]
for i in range(3):
    cold, tem = map(str, input().split())
    if cold == 'Y':
        if int(tem) >= 37:
            m[0] += 1
        else:
            m[2] += 1
    else:
        if int(tem) >= 37:
            m[1] += 1
        else:
            m[3] += 1
for i in m:
    print(i, end=" ")
if m[0] >= 2 :
    print('E', end=" ")