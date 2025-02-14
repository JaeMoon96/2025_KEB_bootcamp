# ✅ 믹스인(Mixin) 클래스: 특정 기능만 추가하는 용도
class FlyingMixin:
    """
    FlyingMixin 클래스
    - 포켓몬에게 '날기' 기능을 추가하는 역할을 하는 믹스인 클래스
    - 단독으로 사용되지 않고, 다른 클래스와 함께 사용됨 (다중 상속)
    """
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"


class SwimmingMixin:
    """
    SwimmingMixin 클래스
    - 포켓몬에게 '수영' 기능을 추가하는 역할을 하는 믹스인 클래스
    - FlyingMixin과 마찬가지로 단독으로 사용되지 않음
    """
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."


# ✅ 포켓몬 기본 클래스 (부모 클래스)
class Pokemon:
    """
    Pokemon 클래스 (부모 클래스)
    - 모든 포켓몬이 공통으로 가지는 속성 (name)을 정의
    - 기본적으로는 별도의 능력이 없으며, 다른 클래스로 확장됨
    """
    def __init__(self, name):
        self.name = name  # 포켓몬 이름 저장


# ✅ 리자몽(Charizard) 클래스: Pokemon + FlyingMixin (날기 가능)
class Charizard(Pokemon, FlyingMixin):
    """
    Charizard 클래스 (Pokemon + FlyingMixin 상속)
    - Pokemon의 기본 속성을 가지면서, FlyingMixin을 통해 '날기' 능력을 추가
    - FlyingMixin의 fly() 메서드를 사용할 수 있음
    """
    pass  # 새로운 기능을 추가하지 않고 부모 클래스 기능만 사용


# ✅ 갸라도스(Gyarados) 클래스: Pokemon + SwimmingMixin (수영 가능)
class Gyarados(Pokemon, SwimmingMixin):
    """
    Gyarados 클래스 (Pokemon + SwimmingMixin 상속)
    - Pokemon의 기본 속성을 가지면서, SwimmingMixin을 통해 '수영' 능력을 추가
    - SwimmingMixin의 swim() 메서드를 사용할 수 있음
    """
    pass  # 새로운 기능을 추가하지 않고 부모 클래스 기능만 사용


# ✅ 객체 생성 및 테스트
g1 = Gyarados("갸라도스")  # 갸라도스 객체 생성 (수영 가능)
c1 = Charizard("리자몽")  # 리자몽 객체 생성 (날기 가능)

# ✅ 믹스인 기능 테스트
print(c1.fly())  # 출력: 리자몽이(가) 하늘을 훨훨 날아갑니다~
print(g1.swim())  # 출력: 갸라도스이(가) 수영을 합니다.

#클래스간의 관계중 연관관계 Associtaion(aggregation composition) has a 관계

# ✅ 1. 연관 관계(Association) has a
# 👉 두 개 이상의 클래스가 서로 연결되어 있지만, 독립적으로 존재할 수 있는 관계.
#
# 객체 간 상호작용을 하지만, 한 객체가 다른 객체의 생명 주기를 관리하지 않음.
# 서로 독립적인 객체이므로, 한 객체가 삭제되더라도 다른 객체는 영향을 받지 않음.
# 🔹 연관 관계의 특징
# ✅ 두 객체는 서로 독립적으로 존재 가능 (Trainer와 Pokemon은 서로 없어도 존재할 수 있음)
# ✅ 트레이너가 여러 포켓몬을 가질 수도 있고, 가질 수도 없음 (self.pokemon = None 가능)
# ✅ 트레이너가 사라져도 포켓몬은 남아 있음




# ✅ 2. 집약 관계(Aggregation)
# 👉 부분(Part)이 전체(Whole)에 속하지만, 독립적으로 존재할 수 있는 관계.
# 전체(Whole) 객체가 삭제되더라도 부분(Part) 객체는 계속 존재할 수 있음.
# 느슨한 결합(Loose Coupling)으로, 한 객체가 다른 객체의 생명 주기를 직접 관리하지 않음(life-cycle이 다름).

# 🔹 집약 관계의 특징
# ✅ 전체(Trainer) 객체가 삭제되더라도 부분(Pokemon) 객체는 계속 존재할 수 있음
# ✅ 한 객체가 여러 객체를 포함할 수 있음 (Trainer가 여러 Pokemon을 가질 수 있음)
# ✅ 느슨한 결합(Loose Coupling) → 객체 간 종속성이 적음
#



# ✅ 3. 합성 관계(Composition)
# 👉 부분(Part)이 전체(Whole)에 속하며, 전체가 사라지면 부분도 함께 사라지는 관계.
#
# 전체(Whole) 객체가 삭제되면 부분(Part) 객체도 함께 삭제됨.
# 강한 결합(Strong Coupling) → 부분 객체는 전체 객체 없이는 존재할 수 없음. life-cycle이 같음
# 🔹 합성 관계의 특징
# ✅ 전체(Trainer) 객체가 삭제되면 부분(PokeBall) 객체도 함께 삭제됨
# ✅ 강한 결합(Strong Coupling) → PokeBall은 Trainer 없이 존재할 수 없음
# ✅ 부분 객체(PokeBall)는 전체 객체(Trainer)에 의해 생성됨 (self.pokeball = PokeBall())

#코드 짤때 change update 항상 생각