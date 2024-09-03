""" Fun stuff! """

def fun_func() -> str:
    f = 'Hej'
    g = 'Då'
    ret = f + ' ' + g
    return ret

def fun_gen():
    f = fun_func
    yield f 
    g = 'Då'
    yield g 
    ret = f.__name__ + ' ' + g
    yield ret 
    print('All elements are out!!')
    return 'End of life!'

print(fun_func())
print(fun_gen())

gen = iter(fun_gen())
print(next(gen)) # gen.__next__()
print(next(gen)) # gen.__next__()
print(next(gen)) # gen.__next__()
try:
    print(next(gen)) # gen.__next__()
except StopIteration as e:
    print(e)


gen2 = iter(fun_gen())
for ob in gen2:
    print(ob)
