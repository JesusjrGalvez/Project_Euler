# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


divisors = [i for i in range(1, 10+1, 1)]
print(divisors)


def is_factor(dividend, divisors):
    for div in divisors:
        if dividend % div == 0:
            pass
        else:
            return False
    return True


# Solution with a for loop.
# for i in range(1, 100000000):
#     if is_factor(i, divisors) == False:
#         #print("HI")
#         pass
#     else:
#         print(i)
#         #print("hola")



# Solution with a while loop.
solution = False
counter = 1
while solution == False:
    if is_factor(counter, divisors) == False:
        counter += 1
    else:
        print(counter)
        counter == True
        break

# Solution is 232792560


