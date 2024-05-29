# N자리 4진수

N = int(input())

res = 0
len_num = 0
def choice():
    global res
    global len_num

    if len_num == N:
        res += 1
        return
    if len_num > N:
        return

    for i in range(1,5):
        len_num += i
        choice()
        len_num -= i

choice()

print(res)