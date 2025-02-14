# ✅ 믹스인 클래스: 특정 기능(날기, 수영) 추가
class FlyingMixin:
    """
    FlyingMixin 클래스
    - 포켓몬에게 '날기' 기능을 추가하는 믹스인 클래스
    - 단독으로 사용되지 않고, 다른 클래스와 함께 다중 상속으로 사용됨
    """

    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"


class SwimmingMixin:
    """
    SwimmingMixin 클래스
    - 포켓몬에게 '수영' 기능을 추가하는 믹스인 클래스
    - FlyingMixin과 마찬가지로 단독으로 사용되지 않음
    """

    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."


# ✅ 포켓몬 기본 클래스 (부모 클래스)
class Pokemon:
    """
    Pokemon 클래스 (부모 클래스)
    - 모든 포켓몬이 공통으로 가지는 속성(name)과 기본 공격 기능을 포함
    """

    def __init__(self, name):
        self.name = name  # 포켓몬 이름 저장

    def attack(self):
        """기본 공격 메서드"""
        print("공격~")


# ✅ 리자몽 클래스 (Pokemon + FlyingMixin)
class Charizard(Pokemon, FlyingMixin):
    """
    Charizard 클래스 (Pokemon + FlyingMixin 상속)
    - Pokemon의 기본 속성을 가지면서, FlyingMixin을 통해 '날기' 능력을 추가
    - FlyingMixin의 fly() 메서드를 사용할 수 있음
    """
    pass  # 별도의 추가 기능 없음 (부모 클래스 기능만 사용)


# ✅ 갸라도스 클래스 (Pokemon + SwimmingMixin)
class Gyarados(Pokemon, SwimmingMixin):
    """
    Gyarados 클래스 (Pokemon + SwimmingMixin 상속)
    - Pokemon의 기본 속성을 가지면서, SwimmingMixin을 통해 '수영' 능력을 추가
    - SwimmingMixin의 swim() 메서드를 사용할 수 있음
    """
    pass  # 별도의 추가 기능 없음 (부모 클래스 기능만 사용)


# ✅ 객체 생성 (포켓몬 생성)
g1 = Gyarados("갸라도스")  # 갸라도스 객체 생성 (수영 가능)
c1 = Charizard("리자몽")  # 리자몽 객체 생성 (날기 가능)

# ✅ 출력 코드 (주석을 제거하면 실행됨)
# print(c1.fly())  # "리자몽이(가) 하늘을 훨훨 날아갑니다~" (FlyingMixin 사용 가능)
# print(g1.swim())  # "갸라도스이(가) 수영을 합니다." (SwimmingMixin 사용 가능)

# ✅ 공격 기능 테스트
# c1.attack()  # "공격~" (Pokemon의 attack() 메서드 사용)
# Charizard.attack()  # ❌ 오류 발생: 클래스 메서드가 아니라 인스턴스 메서드이므로 인자가 필요함!
Charizard.attack(c1)  # ✅ "공격~" (클래스에서 직접 호출할 때, 인스턴스를 명시적으로 전달해야 함)

# ✅ 포켓몬 이름 변경 테스트
print(g1.name)  # 출력: 갸라도스
g1.name = "잉어킹"  # 이름 변경
print(g1.name)  # 출력: 잉어킹