"""
수 1부터 시작해서 우측으로부터 시계방향으로 감아 5×5 행렬을 만들면 아래와 같이 됩니다.

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

여기서 대각선 상의 수를 모두 더한 값은 101 입니다.
같은 방식으로 1001×1001 행렬을 만들었을 때, 대각선 상의 수를 더하면 얼마가 됩니까?
"""


import numpy as np

li = np.array([])

li = np.append(li, 1)

for i in range(3, 1002, 2):
    tmp = np.array([])
    tmp = np.append(tmp, i**2)    
    tmp = np.append(tmp, tmp[0]-i+1)
    tmp = np.append(tmp, tmp[1]-i+1)
    tmp = np.append(tmp, tmp[2]-i+1)

    li = np.append(li, tmp)

print(int(sum(li)))
