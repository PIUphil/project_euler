# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

def isPal(num):
	num = str(num)
	for i in range(int(len(num)/2)):
		if num[i]!=num[-i-1]:
			return False
	return True

for i in range(999,800,-1):
	check = False
	for j in range(999,800,-1):
		if isPal(i*j) and i*j>900000:
			print(i*j, i, j)
			check = True
			break
		else:
			if (i-1)**2 > i*(j-1):
				break				
			
	if check==True:
		break	

"""
palList = []
for i in range(100,1000):
	for j in range(100,1000):
		if isPal(i*j):
			palList.append(i*j)

print(max(palList))
"""
