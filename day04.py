# 🔹 클로저(Closure) 바깥족함수의 리턴값이 안쪽함수의 이름임
def out_func(nout):  # 외부 함수 (nout 값을 받아서 저장)
    def inner_func():  # 내부 함수 (외부 변수를 사용하는 클로저)
        return nout * nout  # 외부 함수의 변수 nout을 사용하여 제곱값 반환

    #클로저 함수는 안쪽함수가 바깥쪽함수에서 선언된 변수나 매개변수를 기억해 안쪽함수가 실행될때 기억한 변수를 활용할수있다.

    return inner_func  # 내부 함수 객체를 반환 (실행되지 않음)

# 외부 함수 호출하여 클로저 생성
x = out_func(9)  # out_func(9) 실행 후 inner_func을 반환 (nout=9를 기억하는 함수)

# 출력 확인
print(type(x))   # <class 'function'> -> x는 inner_func을 가리키는 함수 객체
print(x)         # <function out_func.<locals>.inner_func at 0x...> (메모리 주소 출력)
print(x())       # inner_func 실행 -> 9 * 9 = 81

# 🔹 내부 함수(Inner Function) 사용 예제 (클로저가 아님)
# 외부 함수가 즉시 내부 함수를 실행하고 결과를 반환하는 방식
def out_func(nout):
    def inner_func(nin):  # 내부 함수 (nin 값을 받아서 제곱)
        return nin * nin  # 전달된 nin 값을 제곱
    return inner_func(nout)  # inner_func(nout) 실행 후 결과 반환

# 함수 호출과 동시에 실행되므로 결과값이 반환됨
print(out_func(5))  # 5 * 5 = 25