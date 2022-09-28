def add(x, y):
    return x + y

add2 = lambda x, y: x + y

print(add(1, 3))
print(add2(1, 3))


def get_len(string):
    return len(string)


animals = ['dog', 'cat', 'horse', 'alligator']
print(sorted(animals, key=get_len))


print(sorted(animals, key=lambda s: len(s)))

# Return stings that are 3 in length
f = filter(lambda s: len(s)==3, animals)
print(list(f))
