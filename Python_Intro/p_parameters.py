
def add(digit):
    return digit()

def addition():
    return 2+3

print(add(addition ))

print(add(lambda: 2+3))

a = range(10)

print(list(filter(lambda x:x !=6,a)))

print((lambda x:x*3)(5))