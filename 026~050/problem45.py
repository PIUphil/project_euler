"""
삼각수, 오각수, 육각수는 아래 식으로 구할 수 있습니다.
삼각수	 	Tn = n (n + 1) / 2	 	1, 3, 6, 10, 15, ...
오각수	 	Pn = n (3n − 1) / 2	 	1, 5, 12, 22, 35, ...
육각수	 	Hn = n (2n − 1)	 	1, 6, 15, 28, 45, ...
여기서 T285 = P165 = H143 = 40755 가 됩니다.
오각수와 육각수도 되는, 그 다음으로 큰 삼각수를 구하세요.
"""


import numpy as np

tn = np.array([])
pn = np.array([])
hn = np.array([])

for n in range(1,100000):
    tn = np.append(tn, int(n*(n+1)/2))          # 삼각수
    pn = np.append(pn, int(n*(3*n-1)/2))        # 오각수
    hn = np.append(hn, int(n*(2*n-1)))          # 육각수

intersection = list(set(tn) & set(pn) & set(hn))
print(intersection)
