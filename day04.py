# 🔹 소수 판별 함수 (Prime Number Check)
def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean 값으로 리턴하는 함수

    :param n: 판정할 정수 값
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:  # 2 미만의 숫자는 소수가 아님
        return False
    else:
        i = 2
        while i * i <= n:  # 루트(n)까지만 확인 (연산 최적화)
            if n % i == 0:  # 나누어 떨어지는 경우 (소수 아님)
                return False
            i += 1  # 다음 숫자로 증가
        return True  # 나누어 떨어지는 수가 없으면 소수

# 🔹 사용자 입력을 받아 반복 실행하는 메뉴
while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':  # 🔸 화씨 → 섭씨 변환
        fahrenheit = float(input('Input Fahrenheit : '))  # 사용자 입력을 실수(float)로 변환
        celsius = (fahrenheit - 32.0) * 5.0 / 9.0  # 변환 공식 적용
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {celsius:.4f}C')  # 결과 출력 (소수점 4자리)

    elif menu == '2':  # 🔸 섭씨 → 화씨 변환
        celsius = float(input('Input Celsius : '))  # 사용자 입력을 실수(float)로 변환
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0  # 변환 공식 적용
        print(f'Celsius : {celsius}C, Fahrenheit : {fahrenheit:.4f}F')  # 결과 출력 (소수점 4자리)

    elif menu == '3':  # 🔸 단일 숫자 소수 판별
        number = int(input("Input number : "))  # 사용자 입력을 정수(int)로 변환
        if isprime(number):  # 소수 판별 함수 호출
            print(f'{number} is prime number')  # 소수인 경우 출력
        else:
            print(f'{number} is NOT prime number!')  # 소수가 아닌 경우 출력

    elif menu == '4':  # 🔸 범위 내의 모든 소수 찾기
        n1, n2 = map(int, input("Input first second number : ").split())  # 두 개의 정수를 입력받음
        n1, n2 = min(n1, n2), max(n1, n2)  # 작은 값이 n1, 큰 값이 n2가 되도록 정렬

        # numbers = input("Input first second number : ").split()  # (대체 코드)
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        # if n1 > n2:  # 정렬 처리
        #     n1, n2 = n2, n1

        for number in range(n1, n2 + 1):  # n1부터 n2까지 반복
            if isprime(number):  # 소수인지 판별
                print(number, end=' ')  # 소수인 경우 출력 (공백으로 구분)
        print()  # 줄바꿈

    elif menu == '5':  # 🔸 프로그램 종료
        print('Terminate Program.')  # 종료 메시지 출력
        break  # while 루프 종료

    else:  # 🔸 잘못된 메뉴 선택 시
        print('Invalid Menu!')  # 오류 메시지 출력