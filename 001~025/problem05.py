# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

# LCM 구하기
# 1. 소인수분해하고 딕셔너리로 개수 저장하기 (p.03)
# 2. 최종 딕셔너리와 비교하여 value가 높은것으로 바꾸기
# 3. key * value 하고 모두 합치기


def div(num):
	global so, num0
	
	for i in range(2, num+1):
		if num%i==0:
			so.append(i)
			num0 = int(num/i)
			return
	return

so = []
result = {}						# 소인수분해 중 가장 높은 값들 모음
numDiv = {}						# 각 수 소인수분해
end = 20						# ~20 까지

for i in range(1,end+1):
	result[i] = 0
	numDiv[i] = 0

for num0 in range(1,end+1):
	while num0!=1:
		div(num0)
	#print(so)
		
	for i in so:
		numDiv[i] = so.count(i)
	
	for i in range(1,end+1):
		if result[i] < numDiv[i]:
			result[i] = numDiv[i]
			
	so = []

res = 1
for i in range(1,end+1):
	if result[i]!=0:
		res *= i**result[i]
		#print(i,result[i])
print(res)



# math.lcm(range(1,21))


"""
num = 232792550

while True:
	check = False
	for i in range(2,21):
		if num%i!=0:
			break
		elif i==20:
			print(num)
			check = True
			break
			
	num += 1
	
	if check==True:
		break		
"""
