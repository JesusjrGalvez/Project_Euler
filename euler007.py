# Project Euler problem 007

def is_prime2(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


test_number = 2
counter = 1
while counter != 101:
    if is_prime2(test_number):
        test_number += 1
        counter += 1
    else:
        test_number += 1
print(f"{test_number-1} is the {counter+1-1} prime")

