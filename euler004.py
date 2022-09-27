# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    n_string = str(n)
    n_string_reversed = n_string[::-1]
    if n_string == n_string_reversed:
        return True
    else:
        return False


palindromes = dict()
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        k = i * j
        if is_palindrome(k):
            palindromes[k] = i, j
        else:
            pass

max_product = max(palindromes.keys())
#print(max_product)
max_factors = palindromes.get(max_product)
#print(max_factors)

print(f"The largest palindrome made from the product of two 3 digits numbers is {max_product} and \n"
      f"its factors are {max_factors}")

# Test #2
# # =======
# palindromes = []
# for i, j in zip(range(999, 100, -1), range(999, 100, -1)):
#     k = i * j
#     if is_palindrome(k)== True:
#         palindromes.append(k)
#         print(f"{k} is a palindrome me of {i} * {j}")
#     #break





