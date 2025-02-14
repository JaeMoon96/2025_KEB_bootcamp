# 변수 할당 및 리스트 생성
y = 3  # 변수 y에 3을 할당
x = y * 9  # 변수 x에 y(3) * 9 = 27을 할당
z = list(range(x))  # range(27)의 결과를 리스트로 변환하여 z에 저장
print(z)  # 리스트 z 출력: [0, 1, 2, ..., 26]
print(tuple(map(str, z)))  # z의 모든 요소를 문자열로 변환 후 튜플로 변환하여 출력

# 사용자 정의 range 함수
def my_range(first=0, last=5, step=1):  # 기본값을 가진 매개변수 설정
    number = first  # number를 first 값으로 초기화
    while number < last:  # number가 last보다 작을 때까지 반복
        yield number  # yield를 사용하여 현재 number 값을 반환(함수를 종료하지 않음)
        number = number + step  # step만큼 증가

# yield의 개념:
# 일반적인 return은 함수 실행을 종료하지만, yield는 현재 값을 반환한 후에도 함수의 실행 상태를 유지하여 다음 호출 시 이어서 실행됨.

# my_range() 함수를 호출하면 이터레이터 객체가 반환됨
r = my_range()  # 기본값 (0, 5, 1)으로 호출하여 0부터 4까지 생성하는 제너레이터 객체 반환
print(r, type(r))  # <generator object my_range at 0x...> 형태로 출력됨 (제너레이터 객체)

# 제너레이터의 이터레이션
for x in r:  # r을 순회하면서 값을 하나씩 출력 (0, 1, 2, 3, 4)
    print(x)

# 제너레이터는 한 번만 순회할 수 있음.
# 위의 반복문에서 r을 모두 소모했기 때문에 아래 반복문에서는 출력이 없음.
for x in r:
    print(x)