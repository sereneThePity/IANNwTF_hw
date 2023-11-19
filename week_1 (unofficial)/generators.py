
def meow(n):
    for i in range (0,n):
        yield 'Meow '*(i+1)
        

meowed = meow(3)
print (next(meowed))
print (next(meowed))
print (next(meowed))
