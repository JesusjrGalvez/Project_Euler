# Project Euler problem 009
import math
import time


#Version 1
st = time.time()
perimeter = 1000
triangles = []
for a in range(1, 998):
    for b in range(2, 998):
        c = math.sqrt(a * a + b * b)
        if a + b + c == perimeter:
            triangles.append((a, b, c))

print(triangles)
et = time.time()
print(f"It took {et-st}")

# Version 2
st = time.time()
perimeter = 1000
triangles = []
for a in range(1, 999):
    for b in range(1, 999):
        c = perimeter - a - b
        if c * c == a * a + b * b:
            triangles.append((a, b, c))
print(triangles)
et = time.time()
print(f"It took {et-st}")

# a + b + c = 1000
# a * a + b * b = c * c

