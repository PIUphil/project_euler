# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
# 이 때 10,001번째의 소수를 구하세요.


def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True

primeList = []

i=2
while len(primeList) < 10001:
	if isPrime(i):
		primeList.append(i)
	i+=1

print(primeList[-1])
