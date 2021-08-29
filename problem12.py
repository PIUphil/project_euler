"""
1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 합니다.
예를 들어 7번째 삼각수는 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28이 됩니다.
이런 식으로 삼각수를 구해 나가면 다음과 같습니다.

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
이 삼각수들의 약수를 구해 봅시다.

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
위에서 보듯이, 5개 이상의 약수를 갖는 첫번째 삼각수는 28입니다.

그러면 500개 이상의 약수를 갖는 가장 작은 삼각수는 얼마입니까?
"""


import operator

# 소인수분해
def div(num):
	so = []
	while (num!=1):
		for i in range(2,int(num)+1):
			if num%i==0:
				so.append(i)
				num /= i
				break
	return so

# 약수 개수
def how_many(li):
	count={}				# 원소 개수세기
	for i in li:
	    try:count[i] += 1
	    except:count[i] = 1

	count_plus1 = list(map(operator.add, [1 for _ in range(len(count))], list(count.values())))

	multi = 1
	for i in count_plus1:
		multi *= i

	return multi
		
#print(div(a))
#print(how_many(div(a)))


trinum = []

i=1
j=2
while True:
	trinum.append(i)
	i += j
	j += 1

	if how_many(div(i))>=500:
		print(i)
		break
