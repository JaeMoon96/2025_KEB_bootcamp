#  1  Dictionary Comprehension을 사용하여 숫자의 제곱을 저장하는 딕셔너리 생성
# squares = {n: pow(n, 2) for n in range(10)}  # pow() 함수 사용
# squares = {n: n**2 for n in range(10)}  # ** 연산자 사용
squares = {n: n * n for n in range(10)}  # 곱셈 연산 사용

#  딕셔너리 출력 (0부터 9까지의 숫자와 그 제곱값)
print(squares)
# 출력: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#  2️ 문자열의 각 문자가 몇 번 등장하는지 세는 딕셔너리 생성 (Dictionary Comprehension 사용)
univ = 'inha university'  # 대상 문자열

counts_alphabet = {letter: univ.count(letter) for letter in univ}  # 각 문자별 등장 횟수를 저장

#  결과 출력
print(counts_alphabet)
# 출력 예시 (문자의 개수에 따라 다를 수 있음):
# {'i': 2, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 2, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

#  3️ 같은 기능을 반복문으로 구현 (Dictionary Comprehension 사용하지 않음)
counts_alphabet = dict()  # 빈 딕셔너리 생성

# 문자열을 순회하면서 각 문자의 등장 횟수를 계산
for letter in univ:
    counts_alphabet[letter] = univ.count(letter)  # count() 함수를 사용하여 문자 개수 계산

#  결과 출력 (Dictionary Comprehension을 사용한 방식과 동일한 결과)
print(counts_alphabet)

#  정리
# - `{n: n*n for n in range(10)}` → 0~9의 숫자와 그 제곱값을 저장하는 딕셔너리
#    ✅ 장점: 짧고 간결함
#    ❌ 단점: 없음
#
# - `{letter: univ.count(letter) for letter in univ}` → 문자열에서 각 문자의 등장 횟수를 저장
#    ✅ 장점: 간결하고 가독성이 좋음
#    ❌ 단점: `count()`를 여러 번 호출하여 비효율적 (O(n^2) 시간 복잡도)
#
# - `for` 루프 사용 → 같은 기능을 반복문으로 구현
#    ✅ 장점: 더 명확한 흐름을 가짐
#    ❌ 단점: 코드가 길어질 수 있음
#
#개선 가능 포인트
# 현재 코드에서는 `univ.count(letter)`를 문자열 내 모든 문자에 대해 반복 실행하기 때문에 **비효율적**입니다.
# 아래와 같이 `collections.Counter`를 사용하면 더 빠르게 구현할 수 있습니다.
#
# ```python
# from collections import Counter
#
# univ = 'inha university'
# counts_alphabet = dict(Counter(univ))
#
# print(counts_alphabet)
# ```
#
#**Counter를 사용하면 반복적으로 `count()`를 호출할 필요 없음**
#**속도 개선 효과 (O(n) 시간 복잡도)**