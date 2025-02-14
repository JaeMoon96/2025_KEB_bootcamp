# ✅ 1. 클래스 정의 없이 인스턴스 속성 추가하는 방식

# 포켓몬 클래스를 정의하지만, 아무 기능이 없는 상태 (pass 사용)
class Pokemon:
    pass  # 클래스의 구조만 만들고 실제 기능은 없음

# 포켓몬 객체 생성
pikachu = Pokemon()  # pikachu 인스턴스 생성
squirtle = Pokemon()  # squirtle 인스턴스 생성

# pikachu 객체에 개별 속성 추가
pikachu.name = "피카츄"  # pikachu 인스턴스에 name 속성 추가
pikachu.nemesis = squirtle  # pikachu의 라이벌(nemesis)로 squirtle 객체 설정

# 피카츄의 이름 출력
print(pikachu.name)  # 출력: 피카츄

# 아직 squirtle 객체에는 name 속성이 정의되지 않아서 아래 코드는 오류 발생 가능
# print(pikachu.nemesis.name)  # 오류 발생 가능 (squirtle.name이 정의되지 않았음)

# squirtle 객체에 name 속성을 동적으로 추가
pikachu.nemesis.name = "꼬부기"  # 실제로는 squirtle.name = "꼬부기"와 동일한 동작

# squirtle의 이름을 출력 (위에서 추가했기 때문에 정상적으로 출력됨)
print(pikachu.nemesis.name)  # 출력: 꼬부기
print(squirtle.name)  # 출력: 꼬부기 (pikachu.nemesis는 squirtle을 가리키므로 동일한 객체)

"""
✅ 1. 실행 결과:
피카츄
꼬부기
꼬부기
"""

# ✅ 2. 클래스를 활용한 객체 생성 및 메서드 추가

# 포켓몬 클래스 정의
class Pokemon:
        def __init__(self, name):  # 생성자
        """
        객체가 생성될 때 자동으로 실행되는 메서드.
        :param name: 포켓몬의 이름 (문자열)
        """
        self.name = name  # 포켓몬 이름을 인스턴스 변수로 저장
        print(f"{name} 포켓몬스터 생성")  # 객체 생성 시 메시지 출력

    def attack(self, target):  # 공격 메서드
        """
        다른 포켓몬을 공격하는 메서드.
        :param target: 공격 대상 (Pokemon 객체)
        """
        print(f"{self.name}이(가) {target.name}을(를) 공격!")  # 공격 메시지 출력

# 🔹 포켓몬 객체 생성
charizard = Pokemon("리자몽")  # "리자몽" 객체 생성 → 생성자 실행됨
pikachu = Pokemon("피카츄")  # "피카츄" 객체 생성 → 생성자 실행됨
squirtle = Pokemon("꼬부기")  # "꼬부기" 객체 생성 → 생성자 실행됨

# 🔹 포켓몬 공격 실행
charizard.attack(squirtle)  # 리자몽이 꼬부기를 공격

# 🔹 개별 포켓몬의 이름 출력 (주석 처리된 부분은 이름을 가져오는 코드)
# print(pikachu.name)  # 피카츄
# print(squirtle.name)  # 꼬부기

"""
✅ 2. 실행 결과:
리자몽 포켓몬스터 생성
피카츄 포켓몬스터 생성
꼬부기 포켓몬스터 생성
리자몽이(가) 꼬부기를 공격!
"""

# 1️⃣ 첫 번째 코드 블록
#
# Pokemon 클래스를 정의했지만 아무 기능이 없음.
# pikachu와 squirtle 객체를 생성하고, 동적으로 속성을 추가함.
# pikachu.nemesis = squirtle을 통해 객체 간 관계를 설정.
# pikachu.nemesis.name = "꼬부기" → 실제로 squirtle.name = "꼬부기"와 같은 의미.
# 2️⃣ 두 번째 코드 블록
#
# Pokemon 클래스에 생성자(__init__())와 공격 메서드(attack()) 추가.
# 포켓몬 객체를 만들 때 __init__()이 자동 실행되면서 포켓몬이 생성됨.
# attack() 메서드를 사용하여 포켓몬 간 공격 기능 구현.

# 🔥 이 코드로 배울 수 있는 것
# ✅ 클래스를 정의하는 방법
# ✅ 객체를 생성하고 속성을 추가하는 방법
# ✅ 객체 간 관계 설정 (pikachu.nemesis = squirtle)
# ✅ 메서드를 사용하여 객체 간 상호작용 (attack()) 구현