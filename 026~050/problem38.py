"""
수 192에 1, 2, 3을 각각 곱합니다.
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
곱한 결과를 모두 이어보면 192384576 이고, 이것은 1 ~ 9 팬디지털(pandigital) 수입니다. 이런 과정을 편의상 '곱해서 이어붙이기'라고 부르기로 합니다.
같은 식으로 9와 (1, 2, 3, 4, 5)를 곱해서 이어붙이면 918273645 라는 1 ~ 9 팬디지털 수를 얻습니다.
어떤 정수와 (1, 2, ... , n)을 곱해서 이어붙였을 때 얻을 수 있는 가장 큰 아홉자리의 1 ~ 9 팬디지털 수는 무엇입니까? (단 n > 1)
"""


def isPandigital(num):
    num = str(num)
    if len(num)!=9:
        return False
    for i in range(1,10):
        if str(i) not in num:
            return False
    return True


result = []
for i in range(1,10000):
    tmp = str(i)
    for j in range(2,10):
        tmp += str(i*j)
        if len(tmp)>=9:
            if isPandigital(tmp):
                result.append(int(tmp))
            break
           
print(max(result))
