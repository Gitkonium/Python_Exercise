## 사용자 정의 함수

## 함수 3 요소
## 1) input 입력값 인자 인수 매개변수 parameter argument
## 2) output 출력값 결과값 return 반환
## 3) 기능 ▶ 함수명

## 선언(정의) != 호출

## 유형 1
def hello():
    pass # 함수 미완성

## 유형 2
def printMessage(name,msg='기본 메세지'): # 기본 인자(디폴트 인자) : JAVA의 오버로딩을 가능하게 함
    print(name+'님의 메세지 : '+msg)

def printInfo(*args): # 가변 인자 → 튜플(변화를 허용하지않는 리스트)
    print(type(args))
    print(args)
    for v in args :
        print(v)

## 유형 3
def makeNum():
    num=1234
    return num

## 유형 4
def calc(args):
    return sum(args), round(sum(args)/len(args),1) # 다중 반환

##사용자에게 정수를 입력받으세요.
##사용자는 올바르게 정수를 입력합니다.
##0이하의 정수가 입력되면 종료됩니다.
##종료되면 입력받은 정수들의 총합과 평균을 출력해주세요.
##단, 평균은 소수점 첫째자리까지만 출력해주세요.
##이런 함수를 만들어주세요!
##정수 입력 >> 12
##정수 입력 >> 23
##정수 입력 >> 2
##정수 입력 >> -1
##총합 = 37
##평균 = 12.3

def solution():
    li=[]
    while True :
        num=int(input('정수 입력 >> '))
        if num<=0 :
            break
        li.append(num)
    a,b=calc(li) # 다중 반환
    print('총합 = ',a)
    print('평균 = ',b)












