# SOLID
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)
import time


def factorial_repetition(n) -> int:
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input())
s = time.time()
print(f"{number}! = {factorial_repetition(number)}")
e = time.time()
print(e-s)