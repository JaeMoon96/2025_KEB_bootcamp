# ✅ 믹스인(Mixin) 클래스: 특정 기능(날기, 수영) 추가
class FlyingMixin:
    """
    FlyingMixin 클래스 (Mixin)
    - 포켓몬에게 '날기' 기능을 추가하는 클래스
    - Pokemon 클래스를 상속받는 포켓몬에게 'fly()' 기능 제공
    """

    def fly(self):
        """
        ✅ 문제가 발생하는 코드
        - self.__name을 사용하지만, Pokemon 클래스에서 정의한 __name은 네임 맹글링(name mangling) 적용됨
        - 즉, self.__name이 존재하지 않음 → AttributeError 발생 가능
        """
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"  # ❌ 오류 발생 가능 (네임 맹글링으로 인해 변수명이 변경됨)


class SwimmingMixin:
    """
    SwimmingMixin 클래스 (Mixin)
    - 포켓몬에게 '수영' 기능을 추가하는 클래스
    - Pokemon 클래스를 상속받는 포켓몬에게 'swim()' 기능 제공
    """

    def swim(self):
        """
        ✅ 문제가 발생하는 코드
        - self.__name을 사용하지만, Pokemon 클래스에서 정의한 __name은 네임 맹글링(name mangling) 적용됨
        - 즉, self.__name이 존재하지 않음 → AttributeError 발생 가능
        """
        return f"{self.__name}이(가) 수영을 합니다."  # ❌ 오류 발생 가능 (네임 맹글링)


# ✅ 포켓몬 기본 클래스 (부모 클래스)
class Pokemon:
    """
    Pokemon 클래스 (부모 클래스)
    - 모든 포켓몬이 공통으로 가지는 속성(name)과 기본 공격 기능을 포함
    - '__name' 변수를 사용하여 private 변수처럼 동작하도록 설정 (네임 맹글링 적용)
    """

    def __init__(self, name):
        """
        ✅ 생성자 (__init__ 메서드)
        - '__name' 변수를 사용하여 캡슐화 (네임 맹글링 적용됨)
        - 실제로는 '_Pokemon__name'으로 내부에서 변경됨
        """
        self.__name = name  # ✅ 네임 맹글링 적용됨 → '_Pokemon__name'으로 변경됨

    def attack(self):
        """✅ 기본 공격 메서드"""
        print("공격~")

    # ✅ Getter 메서드 (@property 사용)
    @property
    def name(self):
        """
        ✅ @property 데코레이터
        - name 속성을 조회할 때 자동으로 실행되는 getter 메서드
        - g1.name → 실제로는 self.__name 값을 반환
        """
        return self.__name  # ✅ 'self.__name'은 '_Pokemon__name'으로 내부적으로 변경됨

    # ✅ Setter 메서드 (@name.setter 사용)
    @name.setter
    def name(self, new_name):
        """
        ✅ @name.setter 데코레이터
        - name 속성을 변경할 때 자동으로 실행되는 setter 메서드
        - g1.name = "잉어킹" → self.__name 값 변경됨
        """
        self.__name = new_name  # ✅ '_Pokemon__name'이 변경됨


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

# ✅ property를 사용하여 속성을 직접 변경하는 방법 (@property 자동 호출)
"""
✅ @property를 사용한 속성 접근
- g1.name → 실제로는 name() getter 실행됨
- g1.name = "잉어킹" → 실제로는 name() setter 실행됨
"""
print(g1.name)  # ✅ name 속성에 접근 → 실제로는 name() getter 호출됨 → 출력: 갸라도스

# ❌ 직접 __name 접근 (오류 발생 가능)
# print(g1.__name)  # AttributeError 발생 → '__name'은 직접 접근할 수 없음 (네임 맹글링)

# ✅ _Pokemon__name을 사용하여 직접 접근 가능 (실제로는 private 개념이 아님)
g1._Pokemon__name = "잉어킹"  # ✅ 네임 맹글링된 속성 직접 변경
print(g1.name)  # ✅ 변경된 값 출력 → 출력: 잉어킹
print(g1._Pokemon__name)  # ✅ '_Pokemon__name'으로 직접 접근 가능 → 출력: 잉어킹

"""
✅ Python의 private 개념이 완벽하지 않은 이유

1. '__name'을 사용하면 네임 맹글링이 적용되어 '_Pokemon__name'으로 변경됨.
2. 하지만, '_Pokemon__name'을 사용하면 **외부에서도 직접 접근 가능**하여 private 개념이 깨짐.
3. 즉, **Python에서는 완벽한 private 변수가 없으며, 단순히 네임 맹글링을 통해 변수를 숨기는 역할만 함**.
4. '__name'을 사용해도 '_Pokemon__name'을 통해 값을 변경할 수 있어, 보호 기능이 제한적임.
5. 따라서, Python에서는 private 변수를 강제적으로 숨길 수 없으며, **개발자의 코드 컨벤션에 따라 보호하는 개념이 강함**.
"""