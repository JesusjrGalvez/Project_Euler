# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


primes = []


# Function find_prime v.1
# =======================

def is_prime(n):
    i = 2
    for i in range(2, n+1):
        if n % i == 0 and n != i:
            return False
        if i == n:
            return True


# Function find_prime v.2
# =======================

def is_prime2(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Function find_prime v.3
# =======================
def is_prime3(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



prime_factors = []
for i in range(1, 100000):
    if is_prime2(i) == True:
        print(i)
        prime_factors.append(i)
    else:
        pass

print(prime_factors.pop())


