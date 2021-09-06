# 대칭수(palindrome)인 585는 2진수로 나타내도 10010010012가 되어 여전히 대칭수입니다.
# 10진법과 2진법으로 모두 대칭수인 1,000,000 미만 수의 합을 구하세요.
# (주의: 첫번째 자리가 0이면 대칭수가 아님)


def isPal(num):
	num = str(num)
	for i in range(int(len(num)/2)):
		if num[i]!=num[-i-1]:
			return False
	return True

i2 = 0
li = []
for i in range(1,1000000):
    if isPal(i):
        i2 = format(i, 'b')
        if isPal(i2):
            li.append(i)

print(sum(li))
