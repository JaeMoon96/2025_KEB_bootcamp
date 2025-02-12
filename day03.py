import random  #  랜덤 모듈을 불러옴 (랜덤 추천 기능을 위해 사용)

#  딕셔너리 생성 (기본적인 술과 어울리는 안주 매칭)
drinks_foods = {
    "위스키": "초콜릿",
    "와인": "치즈",
    "소주": "삼겹살",
    "고량주": "양꼬치"
}

#  딕셔너리 출력 (테스트용)
# print(drinks_foods)

#  특정 키 삭제 (`pop()` 사용)
# print(drinks_foods.pop("고량주"))  # '고량주' 삭제 및 해당 값 반환
# print(drinks_foods)  # '고량주' 삭제 후 딕셔너리 출력

#  `del`을 사용하여 키 삭제
# del drinks_foods["위스키"]

#  새로운 항목 추가
# drinks_foods["사케"] = "광어회"

#  일본 술과 안주 추가 (다른 딕셔너리와 병합)
japan_drinks_foods = {
    "사케": "광어회",
    "위스키": "낙곱새"
}
drinks_foods.update(japan_drinks_foods)  # drinks_foods에 japan_drinks_foods 내용 추가

#  딕셔너리의 key 목록을 리스트로 변환
drinks_foods_keys = list(drinks_foods)  # ["와인", "소주", "사케", "위스키", "고량주"]

#  리스트 관련 테스트 코드 (주석 처리)
# print(drinks_foods_keys)
# print(drinks_foods_keys.pop(0))  # 리스트 첫 번째 요소 제거 후 반환
# print(drinks_foods_keys.remove("위스키"))  # 특정 요소 제거
# print(drinks_foods_keys)
# print(random.choice(drinks_foods_keys))  # 리스트에서 랜덤 선택

# 📌 사용자 입력을 받아 추천 시스템 실행
while True:
    menu = input(f'다음 술 중에 고르세요.\n'
                 f'1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   '
                 f'3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   '
                 f'5) {drinks_foods_keys[4]}   6) 아무거나   7) 종료 : ')

    # 사용자가 입력한 값에 따라 적절한 응답 출력
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
    elif menu == '5':
        print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다')
    elif menu == '6':  # 랜덤 추천 기능
        random_drink = random.choice(drinks_foods_keys)  # 랜덤으로 하나 선택
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
    elif menu == '7':  # 프로그램 종료
        print(f'다음에 또 오세요')
        break  # 반복문 종료
    else:
        print("올바른 번호를 입력하세요!")  # 잘못된 입력 처리

#  정리
# - `drinks_foods` → 기본 술과 어울리는 안주 저장
# - `pop()` / `del` → 특정 key 삭제
# - `update()` → 두 개의 딕셔너리를 병합
# - `list(drinks_foods)` → 딕셔너리 key 목록을 리스트로 변환
# - `random.choice()` → 리스트에서 랜덤 요소 선택 (랜덤 추천 기능)
# - `while True` → 무한 루프를 사용하여 사용자의 입력을 지속적으로 받음
# - `if-elif-else` → 사용자의 선택에 따라 적절한 안주를 출력
# - `break` → 사용자가 '7'을 선택하면 프로그램 종료

star = ['테란', '저그', '프로토스']
print(random.choice(star))
print(random.randint(1,6))
print(star[random.randint(0,2)])
