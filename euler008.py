# This is a test


n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# n = 12342211256
print(n)
n_string = str(n)


# print(n_string)
# print(len(n_string))
# print(n_string[4:8])


# This slices "string_" into sections of length length.
def my_slice(string_, length):
    slices = []
    for i in range(len(string_)):
        slices.append((string_[i:i + length]))
    return slices


slices_ = my_slice(n_string, 13)

# This iterates through the sections and computes the product of its numbers.
# Then it returns a dictionary where k, v is "slice, product"
mydict = {}
for slice_ in slices_:
    product = 1
    integers_ = list(map(int, slice_))  # Convert slice of strings to list of integers
    for integer_ in integers_:
        product *= integer_
    mydict.update({slice_: product})

# for k,v in mydict.items():
#    print(k, ":", v, ",")


max_value = max(mydict, key=mydict.get)
key_with_max_value = max(mydict.values())

print("--------")
print(max_value)
print(key_with_max_value)
