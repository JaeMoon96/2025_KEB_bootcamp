from operator import truediv

n = int(input("Input number : "))
is_prime = True

if n >=2:
     for i in range(2 , n):
         if n % i == 0:
            is_prime = False #count = count +1
            break

        else
        is_prime = True

        if count == 0:
            print(f"{n} is prime number")
        else:
            print(f"{n} is NOT prime number!")


n = int(input("Input number: "))
is_prime = True

if n >= 2:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break  # 약수가 발견되면 즉시 종료

    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is NOT a prime number!")
else:
    print(f"{n} is NOT a prime number!")  # 2 미만의 수는 소수가 아님
#dan = input("Intput dan : ")  함수는 문자열 처리라 9 x2 = 99 이런식으로 출력됨

#dan =  int(input("input dan :"))
#for i in range(1, 10, 1):
#    print(f"{dan}*{i}= {dan*i}")



#for dan in range(2, 10, 1):
#    for i in range(1, 10 , 1):
#        print(f"{dan}*{i}={dan*i}")

n = int(input("Input number : "))
is_prime = True
if n >= 2:
    #for i in range(2, n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False  #count = count + 1
            break
        print(i, end=' ')
else:
    is_prime = False

#if count == 0:
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")