<<<<<<< HEAD
=======
def my_abs(n) -> int:
    """
    Return absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n < 0:
        return -n
    return n

def jm_fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수 (재귀함수 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


def jm_fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수 (반복문 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]
>>>>>>> parent of fc79a4d (v4.4 day5)
