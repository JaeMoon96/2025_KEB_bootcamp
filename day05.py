# ✅ 믹스인(Mixin) 클래스: 특정 기능(날기, 수영) 추가
class FlyingMixin:
    """
    FlyingMixin 클래스 (Mixin)
    - 포켓몬에게 '날기' 기능을 추가하는 클래스
    - 독립적으로 사용되지 않고, Pokemon 클래스와 함께 사용됨 (다중 상속)
    """

    def fly(self):
        return f"{self.hidden_name}이(가) 하늘을 훨훨 날아갑니다~"  # ✅ hidden_name 사용


class SwimmingMixin:
    """
    SwimmingMixin 클래스 (Mixin)
    - 포켓몬에게 '수영' 기능을 추가하는 클래스
    - FlyingMixin과 마찬가지로 독립적으로 사용되지 않음
    """

    def swim(self):
        return f"{self.hidden_name}이(가) 수영을 합니다."  # ✅ hidden_name 사용


# ✅ 포켓몬 기본 클래스 (부모 클래스)
class Pokemon:
    """
    Pokemon 클래스 (부모 클래스)
    - 모든 포켓몬이 공통으로 가지는 속성(name)과 기본 공격 기능을 포함
    - 'name' 속성을 직접 접근하지 않고, getter/setter를 통해 관리 (property 사용)
    """

    def __init__(self, name):
        """
        ✅ 생성자 (__init__ 메서드)
        - Pokemon 객체를 생성할 때 호출됨
        - name 속성을 직접 저장하지 않고, hidden_name 속성에 저장 (캡슐화)
        """
        self.hidden_name = name  # ✅ 실제 이름을 저장하는 속성 (비공개처럼 사용)

    def attack(self):
        """✅ 기본 공격 메서드"""
        print("공격~")

    # ✅ Getter 메서드 (이름을 반환)
    def get_name(self):
        """
        ✅ Getter (name 조회)
        - hidden_name 값을 반환하는 역할
        """
        return self.hidden_name

    # ✅ Setter 메서드 (이름을 변경)
    def set_name(self, new_name):
        """
        ✅ Setter (name 변경)
        - hidden_name 값을 변경하는 역할
        """
        self.hidden_name = new_name

    # ✅ property()를 사용하여 name 속성을 getter/setter로 설정
    """
    ✅ property()의 사용 장점
    1. 속성처럼 사용 가능
       - g1.get_name() 대신 g1.name을 사용하여 가독성 향상
       - g1.set_name("잉어킹") 대신 g1.name = "잉어킹"을 사용 가능

    2. 데이터 보호 (캡슐화)
       - hidden_name을 직접 수정하지 않고, getter/setter를 통해 값 변경 가능

    3. 데이터 검증 가능
       - set_name()을 수정하여 특정 조건이 충족되지 않으면 값 변경을 막을 수 있음

    4. 유지보수 용이
       - 속성 접근 방식 변경 시, 내부 getter/setter만 수정하면 됨
    """
    name = property(get_name, set_name)


# ✅ 리자몽 클래스 (Pokemon + FlyingMixin)
class Charizard(Pokemon, FlyingMixin):
    """
    Charizard 클래스 (Pokemon + FlyingMixin 상속)
    - Pokemon의 기본 속성을 가지면서, FlyingMixin을 통해 '날기' 능력을 추가
    """
    pass  # 추가 기능 없음 (부모 클래스 기능만 사용)


# ✅ 갸라도스 클래스 (Pokemon + SwimmingMixin)
class Gyarados(Pokemon, SwimmingMixin):
    """
    Gyarados 클래스 (Pokemon + SwimmingMixin 상속)
    - Pokemon의 기본 속성을 가지면서, SwimmingMixin을 통해 '수영' 능력을 추가
    """
    pass  # 추가 기능 없음 (부모 클래스 기능만 사용)


# ✅ 객체 생성 (포켓몬 생성)
g1 = Gyarados("갸라도스")  # 갸라도스 객체 생성 (수영 가능)
c1 = Charizard("리자몽")  # 리자몽 객체 생성 (날기 가능)

# ✅ getter/setter를 직접 호출하는 방법
"""
✅ getter/setter 직접 호출 (일반 메서드 방식)
- g1.get_name() → hidden_name 값을 가져옴
- g1.set_name("잉어킹") → hidden_name 값을 변경
"""
# print(g1.get_name())  # 출력: 갸라도스
# g1.set_name("잉어킹")  # 이름 변경
# print(g1.get_name())  # 출력: 잉어킹

# ✅ property를 사용하여 속성을 직접 변경하는 방법 (getter/setter 자동 호출)
"""
✅ property를 사용한 속성 접근
- g1.name → 실제로는 get_name() 실행됨
- g1.name = "잉어킹" → 실제로는 set_name() 실행됨
"""
print(g1.name)  # ✅ name 속성에 접근 → 실제로는 get_name() 호출됨 → 출력: 갸라도스
g1.name = "잉어킹"  # ✅ name 속성을 변경 → 실제로는 set_name() 호출됨
print(g1.name)  # ✅ 변경된 값 출력 → 출력: 잉어킹
