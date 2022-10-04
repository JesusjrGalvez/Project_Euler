def Fibonacci:

    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.max = max

    def __iter__():
        return self

    def next(self):
        if self.a > self. max:
            raise StopIteration

        value_to_be_returned = self.a

        self.a, self.b = self.b, self.a + self.b

        return value_to_be_returned

    def next(self):
