num = list(map(int,input().split()))
l1, l2 = [], []
for i in num:
    if i > 500:
        l2.append(i)
    else:
        l1.append(i)
print(f'{max(l1)} {min(l2)}')