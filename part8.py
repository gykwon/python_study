"""

1. 다음 코드에 대해 틀리게 설명한것 2
  from calculator import plus
    1) calculator 는 모듈 이름이다
    2) plus는 변수의 이름이 절대 아니다  --> import가 접근 가능하게 하는 코드에는 벼수, 함수, 클래스 등 모두 포함된다.
    3) plus는 함수의 이름일 수 있다



2. 다음과 같이 calculator.py가 구현되어 있을 때 보기 중 옳지 않은 모듈 반입 구문을 고르세요 --> 6
 def plus(a,b):
     return a+b

 def minus(a,b):
     return a-b

 def multiply(a,b):
     return a*b;

 def divide(a,b):
     return a/b

    1) import calculator
    2) from calculator import minus
    3) from calculator import plus, minus
    4) from calculator import * --> 가능은 하나 지양해야할 코드 어떤 모듈 또는 어떤 함수를 불러오고 있는지 파악하기 힘들어짐
    5) import calculator as c
    6) import calculator.plus



3. 모듈과 package에 대해서 설명 하세요
모듈의 수가 크게 늘어나도 모듈의 이름이 충돌하거나 찾기 어렵지 않도록 디렉토리 별로 정리하는것
파이썬에서는 이렇게 모듈을 모아놓는 디렉토리를 패키지라고 함
평범한 디렉토리가 파이썬 패키지로 인정받으려면 __init__.py 파일을 그 경로에 갖고 있어야 함

"""