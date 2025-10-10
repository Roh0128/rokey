def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g= simple_generator()

print("__iter__" in dir(g))
print('__next__' in dir(g))

print(type(g))

for item in g:
    print(item)

def mygen():
    for i in range(1,100):
        result= i*i
        yield result
gen= mygen()
print(next(gen))
print(next(gen))
print(next(gen))