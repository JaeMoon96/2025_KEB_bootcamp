university = "Inha\nUniversity!"
#university = r"Inha\nUniversity!"  # raw string 역슬래쉬 그대로 출력
#print(university)

# slicing
# print(university[:4])   #inha 왼쪽부터 4개
# print(university[:-11]) #inha 오른쪽부터 11개
# print(len(university))  #len 문자열의 길이 16
# print(university[0:len(university)]) #INHA
                                        #University
# print(university[:16])
# print(university[::2])

number1 = input("First number : ")  #5
number2 = input("Second number : ") #3
print(number1 + number2)  # concatenation -> 53
print(number1 * 3)  # duplicate -> 555
print(number1 + 3)  # TypeError: can only concatenate str (not "int") to str