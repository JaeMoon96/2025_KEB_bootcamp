course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB'))
print(course.rfind('KEB'))
print(course.index('KEB'))
print(course.rindex('KEB'))
print(course.find('Inha'))  # -1 find는 찾는게없으면 -1 -> if문으로 -1출력시 예외처리가능
print(course.index('Inha'))  # ValueError: substring not found index는 예외

print(course)
course = course.replace('KEB', 'Inha', 2)
print(course)
print(course.strip())
print(course.strip("!#.*"))


# print(course)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)