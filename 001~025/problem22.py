"""
여기 5천개 이상의 영문 이름들이 들어있는 46KB짜리 텍스트 파일 names.txt 이 있습니다 (우클릭해서 다운로드 받으세요).
이제 각 이름에 대해서 아래와 같은 방법으로 점수를 매기고자 합니다.

먼저 모든 이름을 알파벳 순으로 정렬합니다.
각 이름에 대해서, 그 이름을 이루는 알파벳에 해당하는 수(A=1, B=2, ..., Z=26)를 모두 더합니다.
여기에 이 이름의 순번을 곱합니다.
예를 들어 "COLIN"의 경우, 알파벳에 해당하는 수는 3, 15, 12, 9, 14이므로 합이 53, 그리고 정렬했을 때 938번째에 오므로 최종 점수는 938 × 53 = 49714가 됩니다.

names.txt에 들어있는 모든 이름의 점수를 계산해서 더하면 얼마입니까?
"""


# 파일열기
f = open('names.txt', 'r')      # 파일 열기
li = []

line=f.readline()
line = line.replace('"','')
li=line.split(',')

f.close()                       # 파일 닫기

li.sort()                       # 정렬

# 단어마다 숫자 뽑아 합친 후, 
# 인덱스+1을 곱하여 result에 더하기
n = 0
result = 0
for word in li:
    wordNum = 0
    for i in range(len(word)):
        wordNum += ord(word[i])-64      # 아스키코드값으로 변환 후 -64 (영어대문자)

    result += (li.index(word)+1)*wordNum

print(result)
