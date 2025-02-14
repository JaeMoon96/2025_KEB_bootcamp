import random  # random 모듈을 임포트하여 난수를 생성할 수 있도록 함


# 사용자 정의 예외 클래스 생성
class OopsException(Exception):
    pass  # 별도의 동작 없이 Exception을 상속받아 새로운 예외 유형 생성 상속 (is a로 이어지는 관계) 연관관계 (has a로 이어짐)


# 난수 리스트 생성 (1~100 사이의 랜덤 숫자 10개를 리스트에 저장)
# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)  # 생성된 난수 리스트 출력

try:  # 예외 발생 가능성이 있는 코드를 try 블록에 작성
    pick = int(input(f"Input index (0 ~ {len(numbers) - 1}) : "))  # 사용자 입력을 정수로 변환
    print(numbers[pick])  # 사용자가 입력한 인덱스의 리스트 값을 출력
    print(5 / 2)  # 단순한 연산 수행 (예외 발생 가능성 없음)

    # 강제로 OopsException 예외 발생시키기
    raise OopsException("Oops~~")  # raise를 사용하여 예외 발생

# 예외 처리 블록
except IndexError as err:  # 리스트 인덱스가 범위를 벗어났을 때
    print(f"Wrong index number\n{err}")

except ValueError as err:  # 정수가 아닌 값을 입력했을 때 (예: "abc"를 입력)
    print(f"Input only number~\n{err}")

except ZeroDivisionError as err:  # 0으로 나누는 오류 (현재 코드에서는 발생하지 않음)
    print(f"The denominator cannot be 0.\n{err}")

# except OopsException as err:  # OopsException 예외 발생 시 실행 (현재 주석 처리됨)
#     print(f"Oops Oops {err}")

except Exception as err:  # 위에서 처리하지 못한 모든 예외를 처리 일반적으로 Exception은 제일 아래에 사용 마지막 보험용
    print(f"Error occurs : {err}")

else:  # try 블록에서 예외가 발생하지 않으면 실행되는 블록
    print(f"Program terminate")  # 프로그램 정상 종료 메시지 출력