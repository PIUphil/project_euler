import numpy as np

li = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63,67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


# 끝자리 숫자 
floar = 3#len(li)
endNum = [0,1]
tmp = []
plus1 = 1

for i in range(1,floar-1):
	plus1+=10**i
	
	for j in endNum:
		tmp.append(j+plus1)
	
	endNum += tmp


#endNum = list(map(str, endNum))
endStr = []
for i in endNum:
	endStr.append(str(i).zfill(floar))

#print(endStr,"\n")


# 접근하기
ali = []
for i in range(len(endStr)):
	bli = []
	for j in range(floar):
		bli.append(str(j)+endStr[i][j])
	ali.append(bli)

#print(ali,"\n")


# 최종 숫자합 리스트
resultLi = []

for i in range(len(ali)):
	k=0
	for j in range(floar):
		k += li[int(ali[i][j][0])][int(ali[i][j][1])]

	resultLi.append(k)

#print(resultLi)
resultLi = np.array(resultLi)
print(np.argmax(resultLi))
print(endStr[np.argmax(resultLi)])
print(max(resultLi))
