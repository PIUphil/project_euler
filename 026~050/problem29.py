"""
2 ≤ a ≤ 5 이고 2 ≤ b ≤ 5인 두 정수 a, b로 만들 수 있는 ab의 모든 조합을 구하면 다음과 같습니다.
2²2=4,  2³=8,  2⁴=16,  2⁵=32
3²=9,  3³=27,  3⁴=81,  3⁵=243
4²=16,  4³=64,  4⁴=256,  4⁵=1024
5²=25,  5³=125,  5⁴=625,  5⁵=3125
여기서 중복된 것을 빼고 크기 순으로 나열하면 아래와 같은 15개의 수가 됩니다.

4,  8,  9,  16,  25,  27,  32,  64,  81,  125,  243,  256,  625,  1024,  3125
그러면, 2 ≤ a ≤ 100 이고 2 ≤ b ≤ 100인 a, b를 가지고 만들 수 있는 ab는 중복을 제외하면 모두 몇 개입니까?
"""


import numpy as np

li = np.array([])

for i in range(2, 101):
    for j in range(2, 101):
        li = np.append(li, i**j)

print(len(np.unique(li)))