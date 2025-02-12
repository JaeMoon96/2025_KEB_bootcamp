#  딕셔너리 생성 (술과 어울리는 안주를 매칭)
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}

#  딕셔너리의 key 목록을 리스트로 변환
drinks_foods_keys = list(drinks_foods)  # ["위스키", "와인", "소주", "고량주"]

#  t반복문을 사용하여 사용자 입력을 받아 처리
while True:
    # 사용자에게 선택지를 제공
    menu = input(f'다음 술 중에 고르세요.\n'
                 f'1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   '
                 f'3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) 종료 : ')

    # 사용자가 선택한 번호에 따라 대응하는 안주를 출력
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
    elif menu == '5':  # '5' 입력 시 프로그램 종료
        print(f'다음에 또 오세요')
        break  # 반복문 종료
    else:
        print("올바른 번호를 입력하세요!")  # 잘못된 입력 처리

#  정리
# - `drinks_foods` → 술과 어울리는 안주를 저장하는 딕셔너리
# - `list(drinks_foods)` → 딕셔너리의 key 목록을 리스트로 변환
# - `while True` → 무한 루프를 사용하여 사용자의 입력을 지속적으로 받음
# - `input()` → 사용자가 메뉴 선택 (1~5)
# - `if-elif-else` → 사용자의 선택에 따라 적절한 안주를 출력
# - `break` → 사용자가 '5'를 선택하면 프로그램 종료