#Assignment
#v2,5) while 안쪽에 하드 코딩된 코드를 함수화 하시오

import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삼겹살", "양꼬치"]

def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]} 입니다')


drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"
#drinks.append("데킬라")
#snacks.append("소금")

menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '
print(menu_list)
#menu = input(f'다음 술 중에 고르세요.\n' f'1) {drinks[0]}   2) {drinks[1]}   'f'3) {drinks[2]}   4) {drinks[3]}   'f'5) {drinks[4]}   6) 아무거나   7) 종료 : ')

while True:
    menu = input()
    if menu == '1':
        print_menu(int(menu)-1)
    elif menu == '2':
        print_menu(int(menu)-1)
    elif menu == '3':
        print_menu(int(menu)-1)
    elif menu == '4':
        print_menu(int(menu)-1)
    elif menu == '5':
        print_menu(int(menu) - 1)
    elif menu == '6':
        random_index = random.randint(0, len(drinks)-1)
        #random_index = random.randint(0, 4) 보다는 위의 코드가 메뉴가 업데이트 됐을때 대응하기좋음
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
        # random_drink = random.choice(drinks_foods_keys)
        # print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break

