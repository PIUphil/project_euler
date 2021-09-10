"""
1487, 4817, 8147은 3330씩 늘어나는 등차수열입니다. 이 수열에는 특이한 점이 두 가지 있습니다.
● 세 수는 모두 소수입니다.
● 세 수는 각각 다른 수의 자릿수를 바꿔서 만들 수 있는 순열(permutation)입니다.
1자리, 2자리, 3자리의 소수 중에서는 위와 같은 성질을 갖는 수열이 존재하지 않습니다. 하지만 4자리라면 위엣것 말고도 또 다른 수열이 존재합니다.
그 수열의 세 항을 이었을 때 만들어지는 12자리 수는 무엇입니까?
"""

import numpy as np
from sympy import isprime
from itertools import permutations

for n in range(1000,10000):    
    per = np.array([])
    for i,j,k,l in permutations(str(n)):
        if isprime(int(i+j+k+l)) and i!="0":
            per = np.append(per, int(i+j+k+l))
    
    for ii in per:
        for jj in per:
            for kk in per:
                if ii<jj and jj<kk and jj-ii==kk-jj:
                    print(str(int(ii))+str(int(jj))+str(int(kk)))
