num = list(map(int,input().split()))
l = []
for n in num:
    if n < 250:
        l.append(n)
    else:
        break

len_l = len(l)
sum_l = sum(l)
mean = sum_l/len_l
print(f"{sum_l} {mean:.1f}")