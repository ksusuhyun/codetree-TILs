n = int(input())
score = list(map(float,input().split()))
mean = sum(score)/len(score)
print(f'{mean:.1f}')
if mean >= 4.0:
    print('Perfect')
elif mean >= 3.0:
    print('Good')
else:
    print('Poor')