"""
소수 3797에는 왼쪽부터 자릿수를 하나씩 없애거나 (3797, 797, 97, 7) 오른쪽부터 없애도 (3797, 379, 37, 3) 모두 소수가 되는 성질이 있습니다.
이런 성질을 가진 소수는 단 11개만이 존재합니다. 이것을 모두 찾아서 합을 구하세요.
(참고: 2, 3, 5, 7은 제외합니다)
"""


def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True if (num!=0 and num!=1) else False

#num = 3797


result = []
num = 10

while True:
    if isPrime(num):
        num = str(num)

        li = [num]
        for i in range(len(num)-1):         # 왼쪽부터 없애기
            li.append(num[i+1:])
        for j in range(len(num)-1):         # 오른쪽부터 없애기
            li.append(num[:len(num)-j-1])

        tmp = []
        for j in li:			    # 소수 확인
            tmp.append(isPrime(int(j)))

        if False not in tmp:
            result.append(int(num))

    if len(result)==11:
        break

    num = int(num)
    num += 1

#print(result)
print(sum(result))
