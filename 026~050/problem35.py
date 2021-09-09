"""
소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 원형 소수(circular prime)라고 합니다. 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다.
이런 소수는 100 미만에 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.
그러면 1,000,000 미만에는 모두 몇 개나 있을까요?
"""

def isPrime(num):                     # 소수 확인
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True

def mix(string):                     # 문자 섞기
    string = str(string)
    m = [string]
    for i in range(len(string)-1):
        m.append(m[i][1:]+m[i][0])

    return m[1:]

result = []
for i in range(2, 1000000):
    tmp = []
    if isPrime(i):
        for j in mix(i):
            tmp.append(isPrime(int(j)))
        
        if False not in tmp:
            result.append(i)

print(len(result))
