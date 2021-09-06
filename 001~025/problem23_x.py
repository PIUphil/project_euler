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
