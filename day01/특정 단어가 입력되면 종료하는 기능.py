## 단어를 입력받는다.
## 사용자는 영어로만 입력한다.
## 영단어 입력 >> apple
## 영단어 입력 >> aaaa
## 영단어 입력 >> abanana
## 영단어 입력 >> candy
## 영단어 입력 >> ant
## 영단어 입력 >> engle
## stop이 입력되면 종료한다.
## 입력한 단어들 중에서 a로 시작하는 단어만 datas리스트에 저장해서 출력한다.


## + a가 가장많이 들어간 단어를 출력한다.
## 2개 이상이면 첫 번쨰 단어만 출력한다.

datas = []

index = 0

word = ''

aCount = 0

while True:

    word = input('영단어 입력 >>')

    if word == 'stop':
        
        break

    elif word[0] == 'a':

        datas.append(word)

        print(datas[index])

        index += 1

for i in range(len(datas)):

    if aCount < datas[i].count('a'):

        aCount = datas[i].count('a')

        word = datas[i]


print(word)

    

    

    
