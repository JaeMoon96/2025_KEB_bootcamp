# ✅ 부모 클래스 (Pokemon)
class Pokemon:
    """
    Pokemon 클래스 (부모 클래스)
    모든 포켓몬이 공통으로 가지는 속성과 메서드를 정의
    """

    def __init__(self, name):  # 생성자
        self.name = name  # 포켓몬의 이름 저장

    def attack(self, target):  # 기본 공격 메서드
        """
        포켓몬이 공격하는 기본 메서드 (모든 포켓몬 공통)
        :param target: 공격 대상 (Pokemon 객체)
        """
        print(f"{self.name}이(가) {target.name}을(를) 공격!")


# ✅ 자식 클래스 (Pikachu) - Pokemon을 상속받음
class Pikachu(Pokemon):  # Pikachu is-a Pokemon (상속)
    """
    Pikachu 클래스 (Pokemon을 상속)
    추가 속성: type (공격 타입)
    추가 메서드: electric_info() - 전기 계열 공격 설명
    """

    def __init__(self, name, type):
        """
        Pikachu는 Pokemon의 속성(name)을 상속받고,
        추가적으로 type 속성을 가짐.
        """
        super().__init__(name)  # 부모 클래스(Pokemon)의 생성자 호출
        #self.name = name 을 사용하면 부모 클래스의 생성자(super().__init__(name))를 호출하지 않고 자식 클래스에서
        # self.name = name을 직접 설정하면 코드의 유지보수성과 확장성이 떨어지는 문제가 발생
        # 부모 클래스의 생성자가 실행되지 않음 부모 클래스 변경 시 자식 클래스에 반영되지 않음 다중 상속에서 일부 부모 클래스의 생성자가 실행되지 않을 가능성

        self.type = type  # 추가 속성: 포켓몬 타입

    def attack(self, target):
        """
        attack() 메서드 오버라이딩 (부모 클래스의 메서드를 재정의)
        Pikachu는 전기 속성 공격을 수행함.
        """
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")

    def electric_info(self):
        """Pikachu만의 추가 메서드 - 전기 타입 공격 설명"""
        print("전기 계열의 공격을 합니다")


# ✅ 자식 클래스 (Squirtle) - Pokemon을 상속받음
class Squirtle(Pokemon):  # Squirtle is-a Pokemon (상속)
    """
    Squirtle 클래스 (Pokemon을 상속)
    Pokemon의 모든 속성과 메서드를 그대로 사용 (추가 기능 없음)
    """
    pass  # 추가적인 기능 없이 Pokemon의 기능을 그대로 상속받음


# ✅ Pokemon을 상속받지 않은 클래스 (Agumon)
class Agumon:
    """
    Agumon 클래스 (Pokemon을 상속받지 않음)
    Pokemon의 속성과 메서드를 가지지 않음
    """
    pass  # Pokemon과 관련 없음 (독립적인 클래스)


# ✅ 객체 생성 및 동작 테스트
p1 = Pikachu("피카츄", "전기")  # Pikachu 객체 생성 (이름과 타입 입력)
p2 = Squirtle("꼬부기")  # Squirtle 객체 생성 (Pokemon의 기본 생성자 사용)
p3 = Pokemon("아무개")  # 일반 Pokemon 객체 생성

# ✅ 피카츄는 전기 타입 공격이 가능
p1.electric_info()  # 출력: 전기 계열의 공격을 합니다

# p3는 Pokemon 클래스의 인스턴스이므로 electric_info() 메서드가 없음 → 에러 발생!
# p3.electric_info()  # AttributeError: 'Pokemon' object has no attribute 'electric_info'

# ✅ 피카츄가 꼬부기를 공격 (오버라이딩된 메서드 사용)
p1.attack(p2)  # 출력: 피카츄이(가) 꼬부기을(를) 전기 공격!

# ✅ 꼬부기가 피카츄를 공격 (Pokemon 기본 공격 메서드 사용 꼬부기는 자식클래스에 속성이 오버라이딩되지 않았기 때문)
p2.attack(p1)  # 출력: 꼬부기이(가) 피카츄을(를) 공격!

# ✅ 피카츄의 속성 확인
print(p1.name, p1.type)  # 출력: 피카츄 전기

# ✅ 상속 관계 확인
print(issubclass(Pikachu, Pokemon))  # True → Pikachu는 Pokemon을 상속받음
print(issubclass(Agumon, Pokemon))  # False → Agumon은 Pokemon을 상속받지 않음

"""
✅ 실행 결과:
전기 계열의 공격을 합니다
피카츄이(가) 꼬부기을(를) 전기 공격!
꼬부기이(가) 피카츄을(를) 공격!
피카츄 전기
True
False
"""