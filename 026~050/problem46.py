"""
크리스티안 골드바흐는 모든 홀수인 합성수를 (소수 + 2×제곱수)로 나타낼 수 있다고 주장했습니다.
9 = 7 + 2×1²
15 = 7 + 2×2²
21 = 3 + 2×3²
25 = 7 + 2×3²
27 = 19 + 2×2²
33 = 31 + 2×1²
그러나 이 추측은 잘못되었음이 밝혀졌습니다.
위와 같은 방법으로 나타낼 수 없는 가장 작은 홀수 합성수는 얼마입니까?
"""


import numpy as np
from sympy import isprime

npList = np.array([])               # not_prime_list
for i in range(3, 100000, 2):
    if not isprime(i):
        npList = np.append(npList, i)


for np in npList:
    chk = 0
    sim2 = 0                            # 근접한 2*n^2
    np = int(np)

    for i in range(1, 1000):
        if 2*(i**2)<np and 2*((i+1)**2)>np:
            sim2 = i
            break

    for j in range(sim2, 0, -1):        
        if isprime(int(np-(2*(j**2)))):
            chk = 1
            break

    if chk==0:
        print(np)
        break
