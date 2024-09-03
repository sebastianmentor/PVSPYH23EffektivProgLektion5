class MyCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # __iter__ returnerar iteratorn själv, i detta fall objektet MyCounter
        while self.current < self.end:
            yield self.current
            self.current += 1

    def __next__(self):

        # while self.current < self.end:
        #     yield self.current
        #     self.current += 1

        # raise StopIteration

        if self.current > self.end:
            # StopIteration undantaget kastas när vi har nått slutet
            raise StopIteration
        else:
            # Vi returnerar det nuvarande värdet och ökar räknaren
            current_value = self.current
            self.current += 1
            return current_value

# Användning av iteratorn
counter = MyCounter(1, 5)
print(type(counter))

# Genom att använda 'for'-loopen kan vi iterera över vår egen iterator
for number in counter:
    print(number)