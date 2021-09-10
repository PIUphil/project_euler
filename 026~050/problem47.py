"""
서로 다른 두 개의 소인수를 갖는 수들이 처음으로 두 번 연달아 나오는 경우는 다음과 같습니다.
14 = 2 × 7
15 = 3 × 5
서로 다른 세 개의 소인수를 갖는 수들이 처음으로 세 번 연속되는 경우는 다음과 같습니다.
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
서로 다른 네 개의 소인수를 갖는 수들이 처음으로 네 번 연속되는 경우를 찾으세요. 그 첫번째 수는 얼마입니까?
"""

import numpy as np

# 소인수분해
def div(num):
    so = np.array([])
    result = np.array([])

    while (num!=1):
        for i in range(2,int(num)+1):
            if num%i==0:
                so = np.append(so, i)
                num /= i
                break
    count = {}
    for i in so:
        try: count[i] += 1
        except: count[i]=1

    for j, k in count.items():
        result = np.append(result, int(j**k))

    return result


for i in range(2, 1000000):
    if len(div(i))==4 and len(div(i+1))==4 and len(div(i+2))==4 and len(div(i+3))==4 and len(set(div(i))|set(div(i+1))|set(div(i+2))|set(div(i+3)))==16:
        print(i)
        break
