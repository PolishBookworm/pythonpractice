# Ask the user for a number and determine whether the number is prime or not.

def is_prime(num):
    """determines whether number is prime or not (num cannot be negative); if num = 0 or 1, returns None"""
    if num == 0 or num == 1:
        return None

    for n in range(2, num):
        if num % n == 0:
            return False
    return True

while True:
    num = int(input("? "))
    print(is_prime(num))