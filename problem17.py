'''
1부터 5까지의 수를 영어로 쓰면 one, two, three, four, five 이고,
각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
  예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
  115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.
'''


numnum = {
1:3, 2:3, 3:5, 4:4,
5:4, 6:3, 7:5, 8:5, 9:4, 
10:3, 11:6, 12:6, 13:8, 14:8,
15:7, 16:7, 17:9, 18:8, 19:8,
20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

hdrd = len(list("hundred"))
andd = len(list("and"))

for i in range(2,10):
	for j in range(1, 10):
		numnum[i*10+j] = numnum[i*10]+numnum[j]

li = []

for i in range(1,100):
	li.append(numnum[i])
	
for i in range(100,1001):
	num0 = int(str(i)[:-2]) 
	num1 = int(str(i)[-2:])

	if i%1000==0:
		li.append(len(list("onethousand")))
		#numnum[i] = len(list("onethousand"))
	elif i%100==0:
		li.append(numnum[num0]+hdrd)
		#numnum[i] = numnum[num0]+hdrd
	else:
		li.append(numnum[num0]+numnum[num1]+hdrd+andd)
		#numnum[i] = numnum[num0]+numnum[num1]+hdrd+andd

#print(numnum[1000])
print(sum(li))
