"""
n번째 삼각수는 tn = ½ n (n + 1) 이라는 식으로 구할 수 있는데, 처음 10개는 아래와 같습니다.
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

어떤 영어 단어에 대해서, 각 철자의 알파벳 순서(A=1, B=2, ..., Z=26)를 모두 더한 값을 '단어값'이라 부르기로 합니다. 예를 들어 'SKY'의 단어값은 19 + 11 + 25 = 55가 되는데, 이것은 우연히도 t10과 같습니다.
이렇게 어떤 단어의 단어값이 삼각수일 경우에는 이 단어를 '삼각단어'라 부르기로 합니다.
약 16KB의 텍스트 파일 words.txt에는 2000개 정도의 영어 단어가 수록되어 있습니다. 이 중에서 삼각단어는 모두 몇 개입니까?
"""


# 삼각수 목록
tn = []
for n in range(1,20):
    tn.append(int((n*(n+1))/2))


# 파일읽기
f = open('words.txt', 'r')      # 파일 열기 
li = []

for i in f:
    i=i.replace('"','')
    
li = i.split(",")

f.close()                       # 파일 닫기

n = 0
for word in li:
    wordNum = 0
    for i in range(len(word)):
        wordNum += ord(word[i])-64      # 아스키코드값으로 변환 후 -64 (영어대문자)

    #print(wordNum)
    if wordNum in tn:
        n+=1

print(n,"개")
