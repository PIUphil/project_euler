# 피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?

fibo = [1,2]

i=2
while fibo[len(fibo)-1] < 4000000 :
	fibo.append(fibo[i-2]+fibo[i-1])
	i+=1

print(sum(i for i in fibo if i % 2 == 0))
