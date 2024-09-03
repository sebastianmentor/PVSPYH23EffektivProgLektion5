from functools import cache

@cache
def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-1) + fib(n-2)

def fib_v2(n):
    if n==0: return None
    
    yield 0

    if n==1: 
        return None
    
    yield 1

    if n==2:
        return None
    a,b = 0,1
    step = 2
    while step < n:
        a,b = b, a + b
        yield b
        step += 1


for f in fib_v2(10):
    print(f)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibian = iter(fibonacci())
while True:
    print(next(fibian))
    if input('') == 'q': 
        fibian.close()
        break


print(next(fibian))