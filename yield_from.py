def undergenerator():
    yield 1
    yield 2
    yield 3

def huvudgenerator():
    # for val in undergenerator():
    #   yield val
    yield from undergenerator()
    yield from undergenerator()
    yield 4
    yield 5

for val in huvudgenerator():
    print(val)