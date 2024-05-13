import random
import time

def lotto():

    print(time.strftime('로또 구매일: ' + '%x', time.localtime()))

    ## 프로그램이 1부터 100까지의 숫자 중 6자리를 랜덤으로 뽑는다.
    sysNumList = random.sample(range(1,100), 6)

    ## 등수별 금액 배정
    priceList = [[1,100000000],[2,50000000],[3,5000000],[4,50000],[5,1000], [6,0]]

    ## 로또 금액 공지
    print('==========================')
    print('등수별 금액')
    print('1등 1억원')
    print('2등 5000만원')
    print('3등 500만원')
    print('4등 5만원')
    print('5등 1000원')
    print('==========================')
    print('')

    ## 사용자에게 선택권
    print('복권의 종류를 입력해주세요.')
    print('1. 자동')
    print('2. 수동')
    print('')
    
    ## 사용자 지정 번호 리스트
    userNumList = [] 

    while True:

        ## 루프 카운트 변수
        i = 1
        
        ## 문자열 대비
        try:
    
            choice = int(input('입력 >>'))

        except ValueError:

            print('옳바른 입력이 아닙니다. 다시 입력해주세요.')

            continue

         ## 자동
        if choice == 1:
            
            ## 자동 선택 => 랜덤 6숫자 
            userNumList = random.sample(range(1,100), 6)

        ## 수동
        elif choice == 2:

            while True:
                
                ## 7번째에서 루프 탈출
                if i == 7:

                    break

                ## 문자열 대비
                try:
    
                    choice = int(input(str(i) + '번째 번호를 입력해주세요. >>'))

                except ValueError:

                    print('정수를 입력해주세요.')

                    continue

                ## 입력이 중복인 경우
                if choice in userNumList:

                    print('이미 입력하신 숫자입니다.')

                    continue

                ## 입력이 정수가 아닌 경우
                if isinstance(choice, int) == False:

                    print('정수를 입력해주세요.')

                    continue

                ## 입력값 리스트에 저장
                userNumList.append(choice)
                
                ## 루프 카운트 1 증가
                i = i + 1


        ## 수동 자동 이외
        else:

            print('옳바른 입력이 아닙니다. 다시 입력해주세요.')
            
            continue

        ## 최상위 로프 탈
        break

    print('')
    print('당첨 번호는' + str(sysNumList) + '입니다.')
    print('')
    print('고객님의 번호는' + str(userNumList) + '입니다.')
    print('')

    ## 프로그램과 사용자의 숫자 교집합
    sameNumList = set(sysNumList) & set(userNumList)

    ## 일치하는 번호가 없는 경우
    if int(len(sameNumList)) == 0:
        
        print('일치하는 번호가 없습니다.')
        
    ## 일치하는 번호가 있는 경우
    else:
    
        print('일치하는 번호는 ' + str(sameNumList) + '로 ' + str(len(sameNumList)) + '개의 숫자가 일치합니다.')
        print('')

        for list in priceList:

            if int(list[0]) == 7 - int(len(sameNumList)):

                print('등수:' + str(list[0]) + ' 금액: ' + str(list[1]))

                

    


    
    
    
    
