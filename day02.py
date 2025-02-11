# Assignment Day 02
# v1.1) Change the for phrase to the while phrase.
# v1.2) Write a program that receives two numbers and outputs only prime numbers between the two numbers. Then, use only the while statement and include the two numbers entered.
# v1.3) Rewrite the code using the power function instead of the ** operator.
# v1.4) Make my_pow custom function instead of ** operator, power function and make it work.

def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i < (int(num ** 0.5) + 1):
        #for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

# main
#help(abs)
#help(is_prime)
n = int(input("Input number : "))

if is_prime(n):  # function call
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")