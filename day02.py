# 1) for -> while  v1.1
# 2) while 구문으로 구간 소수를 출력하는 프로그램을 작성 v1.2
# 3) ** 대신 pow 함수 v1.3



def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i <= int(num ** 0.5):
            if num % i == 0:
                return False
            i += 1

# main
#help(abs)
help(is_prime)
n = int(input("Input number : "))

if is_prime(n):  # function call
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")
