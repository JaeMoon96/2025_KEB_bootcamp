# SOLID
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)
import time

def description_decorator(func):
    def wrapper(*arg):
        print(func.__name__)
        print(func.__doc__)
        r = func(*arg)
        return r
    return wrapper

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper

@time_decorator
@description_decorator

def factorial_repetition(n) -> int:
    """
        factorial function by loop
        :param n:
        :return: results of factorial operation
        """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


number = int(input())
print(f"{number}! = {factorial_repetition(number)}")

# number = int(input())
# ft = time_decorator(factorial_repetition)
# print(f"{number}! = {ft(number)}")
# number = int(input())
# print(f"{number}! = {factorial_repetition(number)}")