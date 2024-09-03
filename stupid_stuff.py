def stupid():
    yield 1,2
    yield 3,4
    yield 5,6

# g = stupid()
for key,val in stupid():
    print(key, val)

#print(next(g))