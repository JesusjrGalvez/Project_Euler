# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


divisors = [i for i in range(1, 3+1, 1)]
print(divisors)


#n = 1


def is_factor(dividend, divisors):
    for div in divisors:
        if dividend % div == 0:
            pass
        else:
            return False
    return True


ans = False
c = 1
while ans == False:
    if is_factor(c, divisors) == False:
        c += 1
        print(c)
    else:
        ans = True
        break
        print(f"{c} and {is_factor(c, divisors)}")