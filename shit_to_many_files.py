class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        while True:
            value, self.a, self.b = self.a, self.b, self.a+self.b
            yield value

f = Fib()
print(type(iter(f)))
for i, value in enumerate(f, 1):
    print(value)
    if i > 5:
        break