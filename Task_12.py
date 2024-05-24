""" Write a code to check whether no is prime or not. Condition use function check() to find whether entered no is positive or negative ,if negative then enter the no, And if yes pas no as a parameter to prime() and check whether no is prime or not? """

def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True

def check(num):
    if num < 0:
        print("Please enter a positive number.")
    else:
        if is_prime(num):
            print(f"{num} is prime.")
        else:
            print(f"{num} is not prime.")
        
num = int(input("Enter a number: "))
check(num)