def isPandigital(num):
    num = str(num)
    for i in range(10):             # 0~9 팬디지털
        if str(i) not in num:
            return False
    return True

sosu = [2, 3, 5, 7, 11, 13, 17]
result = []

for i in range(10**9, 10**10):
    chk = True

    if isPandigital(i):
        for j in range(len(sosu)):
            if int(str(i)[j+1:j+4])%sosu[j]!=0:
                chk = False

        if chk==True:
            result.append(i)

print(sum(result))
