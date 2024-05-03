# 함수 vs 메서드
# 내장함수 vs 사용자 정의 함수

# 개발자들이 만들어놓은 유용한 다양한 함수들이 있다.
# 함수들의 묶음이 생기기 시작
# 함수 묶음 == "모듈",라이브러리
# 모듈(모듈안의 함수)을 사용하기 위해서는 "import"(다운로드,설치,install)

# 표준 모듈
import random
import random as r
##from 모듈명 import 함수명
##from 모듈명 import 함수명1,함수명2,함수명3
##from 모듈명 import *
##from 모듈명 import 함수명 as 함수별칭

##>>> r.randrange(1,10)
##>>> r.randint(1,10)
##>>> li = [11,21,-2,34,5]
##>>> r.choice(li)
##>>> r.shuffle(li)
##>>> li=r.sample(range(1,46), 6)

##>>> import time
##>>> time.sleep(2)

##>>> import math
##>>> math.pow(2,10)
##>>> math.floor(3.141592)
##>>> math.pi



## UP DOWN 게임  OR  로또 게임
## 구현한 내용 블로그에 작성하고 링크 보내기
## 필수 조건 1) 설계서를 먼저 보여줄 것
## 필수 조건 2) 작성하면서 발생한 에러를 설명할 것
## 필수 조건 3) 표준 모듈을 2개이상 사용할 것



li=r.sample(range(1,46), 6)
li.sort()
print(li)
print('총합= '+str(sum(li)))
print('평균= '+str(sum(li)/len(li)))

# 외부 모듈
# 표준 모듈 외에 별도의 설치를 통해 사용할 수 있는 모듈
# 패키지(모듈 집합) 설치 관리자 pip

import numpy as np
print('numpy로 구한 총합= '+str( np.sum(li) ))
print('numpy로 구한 평균= '+str( np.mean(li) ))


