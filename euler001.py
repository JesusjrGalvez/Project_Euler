# Problem 001 from Project Euler

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.


# Find the sum of all the multiples of 3 or 5 below 1000.

result = 0
# Result as a for loop

# for n in range(3, 999):
#     if n % 3 == 0:
#         result += n
#     elif n % 5 == 0:
#         result += n
#     else:
#         pass


# Result as a list comprehension
result = sum(x for x in range(999) if (x % 3 == 0 or x % 5 == 0))
result = sum(x for x in range(999) if (x % 3 == 0 or x % 5 == 0))


print(result)
