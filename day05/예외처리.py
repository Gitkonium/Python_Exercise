 예외처리 : 프로그램의 비정상 종료를 예방하기 위함

# 데이터 가공 작업 중에 에러,예외 등이 발생
# 1) 무시하고 계속  2) 처리
# 어떠한 데이터가 입력되어도,
# 전체 프로그램은 멈춰서는 안된다!

try :
    print('a')
    num=10/1
    print('num= '+str(num))
    print('b')
except ZeroDivisionError :
    print('c')
except Exception as msg :
    print('예외 발생 : ',end='')
    print(msg)
else :
    print('예외가 발생하지않았을때 출력')
finally :
    print('항상 출력')
