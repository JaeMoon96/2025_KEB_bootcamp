mport copy  # copy 모듈을 불러옴

# subjects 리스트 생성 (얕은 복사와 깊은 복사의 차이를 확인하기 위해 중첩 리스트 포함)
subjects = ["a", ["b", "c"], "d"]

# 변수 할당 (같은 객체를 참조)
a = subjects  # a는 subjects와 같은 객체를 참조 (원본과 동일한 주소)

# 얕은 복사(Shallow Copy) - 첫 번째 레벨 요소만 복사, 중첩 리스트는 원본과 공유됨
b = subjects.copy()  # 얕은 복사 (첫 번째 레벨만 복사됨)
c = list(subjects)   # list()를 사용한 얕은 복사 (b와 같은 방식)
d = subjects[:]      # 슬라이싱을 사용한 얕은 복사 (b, c와 같은 방식)

# 깊은 복사(Deep Copy) - 모든 요소를 새로운 객체로 복사
e = copy.deepcopy(a)  # deepcopy는 중첩된 리스트까지 완전히 새로운 객체로 복사

# 복사된 객체들을 출력 (모두 원본과 동일한 내용을 가짐)
print(subjects, a, b, c, d, e)

# 원본 리스트의 중첩 리스트 내부 요소 변경
subjects[1][1] = "x"  # 중첩 리스트의 두 번째 요소 "c"를 "x"로 변경 => e만 deepcopy이므로 영향받지않음

# 변경 후 모든 리스트 출력
print(subjects, a, b, c, d, e)