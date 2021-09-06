# 세 자연수 a, b, c 가 피타고라스 정리 a² + b² = c²를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
# 예를 들면 3² + 4² = 9 + 16 = 25 = 5²이므로 3, 4, 5는 피타고라스 수입니다.
# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

for i in range(1,1000):
	check = False
	for j in range(1,1000):
		if i**2 + j**2 - (1000-i-j)**2 == 0:
			print(i*j*(1000-i-j))
			check = True
			break
			
	if check==True:
		break
