def squares(*n) -> list:
    """
    넘겨 받은 여러 개의 숫자에 대해 각각 제곱한 값을 리스트로 반환하는 함수

    :param n: 여러 개의 숫자 (가변 매개변수, tuple 형태로 전달됨)
    :return: 제곱된 숫자들이 담긴 리스트
    """
    return [pow(i, 2) for i in n]  # 리스트 내포(list comprehension)를 사용하여 각 숫자를 제곱 후 리스트로 반환


def run_function(f, *number) -> list:
    """
    함수와 여러 개의 숫자를 받아서 실행하는 함수

    :param f: 실행할 함수 (첫 번째 매개변수)
    :param number: 실행할 함수에 전달할 여러 개의 숫자 (가변 매개변수)
    :return: 실행된 함수의 반환값 (리스트)
    """
    return f(*number)  # 전달받은 함수 f에 가변 매개변수를 풀어서 전달 (*number)


# 함수 호출 예제
print(squares(7, 5, 2))  # [49, 25, 4]
print(run_function(squares, 9, 10))  # [81, 100]g