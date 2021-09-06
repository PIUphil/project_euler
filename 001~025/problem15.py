"""
아래와 같은 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다 (거슬러 가지는 않기로 합니다).
田 => [→→↓↓], [→↓→↓], [→↓↓→], [↓→→↓], [↓→↓→], [↓↓→→]

그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
"""

size = 20

# 파스칼 삼각수
li = [1, 1]
tmpLi = []

for _ in range(size-1):			
	tmpLi.insert(0,1)
	for i in range(len(li)-1):
		tmpLi.append(li[i]+li[i+1])
		
	tmpLi.append(1)
	li = tmpLi
	tmpLi = []

squareLi = [i*i for i in li]
print(sum(squareLi))
