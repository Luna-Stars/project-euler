# Project Euler
# Alex Johnson
# Problem 32: Pandigital products

def pandigital(x):
    if len(x) != 9: return False
    for i in range(1, 10):
        if str(i) not in x: return False
    return True

def concat(a, b):
    return str(a) + str(b) + str(a*b)

def pandigitalProduct(a, b):
    num = concat(a, b)
    return pandigital(num)

products = set()
for a in range(0, 100000):
    for b in range(a+1, 1000000):
        if len(concat(a, b)) > 9:
            break
        if pandigitalProduct(a, b):
            products.add(a*b)

print(sum(products))
