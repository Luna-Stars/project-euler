# Project Euler
# Alex Johnson
# Problem 38: Pandigital multiples

def pandigital(x):
    if len(x) != 9: return False
    for i in range(1, 10):
        if str(i) not in x: return False
    return True

for i in range(9387, 9235, -1):
    if pandigital(str(i) + str(2*i)):
        print(str(i) + str(2*i))
        break
