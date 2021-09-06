"""
자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 과잉수라고 합니다.

12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 과잉수 중에서는 가장 작습니다.
따라서 과잉수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 과잉수의 합으로 표현 가능함을 보일 수가 있습니다.
두 과잉수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는 더 이상 이 한계값을 낮출 수 없다고 합니다.

그렇다면, 과잉수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?
"""


# 진약수들의 합
def factor(num):
    fac = [1]           # 약수들 집합
    for i in range(2,num):
        if num%i==0:
            fac.append(i)
    return sum(fac)


overNum = []            # 과잉수
for i in range(1,28123):
    if factor(i)>i:
        overNum.append(i)
    
#print(overNum)

plus = []               # 두 수의 합
for n1 in overNum:
    for n2 in overNum:
        plus.append(n1+n2)


# from itertools import combinations

# comb = list(combinations(overNum, 2))       # 조합시키기
# plus = []
# for i in comb:
#     plus.append(sum(i))


result = 0
for i in range(1,28123):
    if i not in plus:
        result+=i
print(result)
