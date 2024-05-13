## 파일 입출력
## 파이썬 언어 특성상, 파일을 읽어들이는 경우가 매우 많음
## 데이터 => 파일 => 분석, 가공, 시각화

##file=open('test.txt', 'rt') # 파일 읽어들이는 코드
##cnt=0
##while True:
##    line=file.readline()
##    if line == '' :
##        break
##    cnt+=1
##    print(str(cnt)+' '+line)
##file.close()

##with open('test.txt', 'rt') as file :
##    lines=file.readlines()
##    for line in lines :
##        print(line)

# wt : 기존의 내용위에 덮어쓰기 ★ 원본을 지켜야한다 !!!!!
# at : 기존의 내용뒤에 이어쓰기
with open('test.txt', 'at') as file :
    while True :
        msg = input('입력 >> ')
        if not msg :
            break
        file.write(msg)


# quiz.txt 파일에 영단어 1개를 저장해주세요.
# banana
# ______ 입력 >> a
# _a_a_a 입력 >> c
# c는 없습니다!
# _a_a_a 입력 >> b
# ba_a_a 입력 >> n
# banana 정답입니다! :D
# quiz.txt 파일에
# 총 4번만에 정답을 맞추셨습니다. 라고 작성해서 저장해주세요.

