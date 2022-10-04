class fibonacci:
 2
 3    def __init__(self, max=1000000):
 4        self.a, self.b = 0, 1
 5        self.max = max
 6
 7    def __iter__(self):
 8        # Return the iterable object (self)
 9        return self
10
11    def next(self):
12        # When we need to stop the iteration we just need to raise
13        # a StopIteration exception
14        if self.a > self.max:
15            raise StopIteration
16
17        # save the value that has to be returned
18        value_to_be_returned = self.a
19
20        # calculate the next values of the sequence
21        self.a, self.b = self.b, self.a + self.b
22
23        return value_to_be_returned
24
25    def __next__(self):
26        # For compatibility with Python3
27        return self.next()
28
29
30if __name__ == '__main__':
31    MY_FIBONACCI_NUMBERS = fibonacci()
32    for fibonacci_number in MY_FIBONACCI_NUMBERS:
33        print(fibonacci_number)