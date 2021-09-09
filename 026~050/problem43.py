"""
수 1406357289은 0 ~ 9 팬디지털인데, 부분열에 관련된 재미있는 성질을 가지고 있습니다.
d1을 첫째 자릿수, d2를 둘째 자릿수...라고 했을 때, 다음과 같은 사실을 발견할 수 있습니다.
● d2 d3 d4 = 406 → 2로 나누어 떨어짐
● d3 d4 d5 = 063 → 3으로 나누어 떨어짐
● d4 d5 d6 = 635 → 5로 나누어 떨어짐
● d5 d6 d7 = 357 → 7로 나누어 떨어짐
● d6 d7 d8 = 572 → 11로 나누어 떨어짐
● d7 d8 d9 = 728 → 13으로 나누어 떨어짐
● d8 d9 d10 = 289 → 17로 나누어 떨어짐
위와 같은 성질을 갖는 0 ~ 9 팬디지털을 모두 찾아서 그 합을 구하면 얼마입니까?
"""


from itertools import permutations

sosu = [2, 3, 5, 7, 11, 13, 17]
result = []

pan= []             # 팬디지털 0~9
for a0,a1,a2,a3,a4,a5,a6,a7,a8,a9 in permutations("1234567890"):
    pan.append(a0+a1+a2+a3+a4+a5+a6+a7+a8+a9)

for i in pan:
    chk = True
    
    for j in range(len(sosu)):
        if int(i[j+1:j+4])%sosu[j]!=0:
            chk = False

    if chk==True:
        result.append(int(i))

print(sum(result))
