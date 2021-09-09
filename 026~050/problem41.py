"""
1부터 n까지의 숫자를 하나씩만 써서 만든 n자리 숫자를 팬디지털(pandigital)이라고 부릅니다.
2143은 4자리 팬디지털인데, 이 수는 동시에 소수이기도 합니다.
n자리 팬디지털 소수 중에서 가장 큰 수는 무엇입니까?
"""


def isNPandigital(num):
    num = str(num)
    for i in range(1,len(num)+1):
        if str(i) not in num:
            return False
    return True

def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True if (num!=0 and num!=1) else False


result = []
for i in range(10000000):
    if isNPandigital(i) and isPrime(i):
        result.append(i)

print(max(result))
