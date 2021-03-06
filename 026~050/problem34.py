"""
수 145는 신기한 성질이 있습니다. 각 자릿수의 팩토리얼(계승)을 더하면  1! + 4! + 5! = 1 + 24 + 120 = 145 처럼 자기 자신이 됩니다.
이렇게 각 자릿수의 팩토리얼을 더하면 자기 자신이 되는 모든 수의 합을 구하세요.
단, 1! = 1 과 2! = 2 의 경우는 덧셈이 아니므로 제외합니다.
"""

def fac(num):
    k = 1
    for i in range(num,0,-1):
        k *= i
    return k

tot = 0
for i in range(1,100000):   
    tmp = []
    tmpNum = 0
    for j in str(i):
        tmpNum += fac(int(j))
    
    tmp.append(tmpNum)
    if i == tmp[-1]:
        tot+=i

print(tot-3)
