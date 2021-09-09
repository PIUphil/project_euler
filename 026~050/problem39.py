"""
세 변의 길이가 모두 자연수 {a, b, c}인 직각삼각형의 둘레를 p 로 둘 때, p = 120 을 만족하는 직각삼각형은 아래와 같이 세 개가 있습니다.
{20, 48, 52}, {24, 45, 51}, {30, 40, 50}
1000 이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마입니까?
"""


result = []
for p in range(3,1001):
    tmp = []
    for i in range(1,p):
        for j in range(1,p):
            k = p-i-j
            if i<=j and i<k and j<k and (k < i+j) and (i**2+j**2==k**2):
                tmp.append((i,j,k))
    result.append(len(tmp))

print(result.index(max(result))+1)
