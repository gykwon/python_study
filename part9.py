from test import *



"""
1. 클래스, 객체, 인스턴스는 서로 어던 점이 다른가
    - 클래스   : 변수와 함수를 객체로 응집 시키려면 클래스가 필요함, 클래스는 자료형 이고 객체는 변수이다
    - 객체    : 객체 = 속성(변수) + 기능(함수), 객체는 클래스의 인스턴스
      ## my_car(객체) = CAR() (클래스) Car 클래스를 my_car객체로 선언함
    - 인스턴스 : 객체 대신 인스턴스라는 용어를 사용하기도 함, 객체 뿐만 아니라 변수도 인스턴스라고 부름

2. 아래 코드에서 오류를 찾고 오류의 원인을 설명하시오

class MyClass:
    def __init__(self):
        self.count = 0


    def increment(self):
        count += 1


3. self 매개변수에 대해 설명
    - 메소드가 소속되어있는 객체


4. 아래 코드에서 B클래스의 __init__() 메소드 안에서 A 클래스의 __init__() 을 호출하게 만들고 싶습니다.
   ㅁ 안에 들어갈 코드는??


    Class A:
        def __init(self):
            self.message = 'Hello'

    Class B:
        def __init(self):
            ㅁㅁㅁㅁㅁ().__init__()
            >> super().__init__()


5. 다음 코드에서 D클래스는 어떤 클래스의 method()를 물려 받았을까?
   ㄴ B : 다이아몬드의 죄악에선 앞에 선언된 클래스의 메소드를 상속 받음
   
    Class A:
        def method(self):
            print("A")


    Class B:
        def method(self):
            print('B')


    Class C(A):
        def method(self):
            print("C")


    class D(B, C):
        pass



6. 다형성은 무엇이며, 오버라이딩과 어떤 관계가 있는지

다형성이란 각 객체가 동일한 인터페이스에 대해 서로 다른 동작을 수행하도록 하는 것을 말한다.
 - 객체가 다형성을 띄면 객체 사용에 있어 편리성이 증대된다.

출처: https://uzooin.tistory.com/138 [뚱땡이 우주인]


오버라이딩
부모 클래스로 부터 상속받은 메소드를 다시 정의


A클래스가 정의되고 B클래스가 A클래스를 상속받음
 - 부모클래스(A), 자식클래스(B)
 - B클래스에서 A클래스의 AA메소드를 재정의 하여 사용하고, A클래스의 AA메소드를 사용 할 수 있는것(super를 통해)
   이런 개념을 다형성 이라고하는거같음
    

"""