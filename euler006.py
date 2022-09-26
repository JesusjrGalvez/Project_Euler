

def sum_of_squares(n):
    # Solution #1
    sol = 0
    for i in range(n+1):
        sol += i * i
    return sol

    # Solution #2
    # yield(sum(x * x) for x in range(n+1))


def square_of_sum(n):
    return sum(range(n+1)) * sum(range(n+1))


print(sum_of_squares(100))
print(square_of_sum(100))
print(range(10))

for j in range(10):
    print(j)
print([j for j in range(10)])

