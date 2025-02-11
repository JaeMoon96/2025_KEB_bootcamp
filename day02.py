#dan = input("Intput dan : ")  함수는 문자열 처리라 9 x2 = 99 이런식으로 출력됨

#dan =  int(input("input dan :"))
#for i in range(1, 10, 1):
#    print(f"{dan}*{i}= {dan*i}")



#for dan in range(2, 10, 1):
#    for i in range(1, 10 , 1):
#        print(f"{dan}*{i}={dan*i}")


    n = int(input("Input number : "))
    cout = 0
    for i in range(1 , n+1):
        if n % i == 0:
            count = count + 1
        if count == 2:
            print(f"{n} is prime number")
        else:
            print(f"{n} is NOT prime number!")