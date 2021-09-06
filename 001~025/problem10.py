# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True

primeSum = 0
for i in range(2,2000001):
	if isPrime(i):
		primeSum+=i

print(primeSum)
