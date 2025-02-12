#Assignment
#v2,2) 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정

import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삼겹살", "양꼬치"]

drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"

while True:
    menu = input(f'다음 술 중에 고르세요.\n' f'1) {drinks[0]}   2) {drinks[1]}   'f'3) {drinks[2]}   4) {drinks[3]}   'f'5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {snacks[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는 {snacks[2]} 입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {snacks[3]} 입니다')
    elif menu == '5':
        print(f'{drinks[4]}에 어울리는 안주는 {snacks[4]} 입니다')
    elif menu == '6':
        random_index = random.randint(0, len(drinks)-1)
        #random_index = random.randint(0, 4) 보다는 위의 코드가 메뉴가 업데이트 됐을때 대응하기좋음
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
        # random_drink = random.choice(drinks_foods_keys)
        # print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break


#  정리
# - `drinks = ["위스키", "와인", "소주", "고량주", "사케"]` → 술 리스트
# - `foods = ["낙곱새", "치즈", "삼겹살", "양꼬치", "광어회"]` → 해당 술에 맞는 안주 리스트
# - 리스트의 인덱스를 활용하여 대응되는 술-안주 매칭
# - `random.randint(0, len(drinks) - 1)` → 리스트에서 랜덤 요소 선택
# - `while True` → 무한 루프를 사용하여 사용자의 입력을 지속적으로 받음
# - `if-elif-else` → 사용자의 선택에 따라 적절한 안주를 출력
# - `break` → 사용자가 '7'을 선택하면 프로그램 종료