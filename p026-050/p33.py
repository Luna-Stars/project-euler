# Project Euler
# Alex Johnson
# Problem 33: Digit cancelling fractions

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def rem(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return string[:i] + string[i+1:]
    return string

def digit_cancel(n, d):
    n_str = str(n)
    d_str = str(d)
    if '0' in n_str + d_str: return (n, d)
    for char in n_str:
        if char in d_str:
            return (int(rem(n_str, char)), int(rem(d_str, char)))
    return (n, d)

def frac_reduce(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

fracs = []

for a in range(10, 100):
    for b in range(a + 1, 100):
        if digit_cancel(a, b) != (a, b):
            cancel_a = digit_cancel(a, b)[0]
            cancel_b = digit_cancel(a, b)[1]
            if frac_reduce(cancel_a, cancel_b) == frac_reduce(a, b):
                fracs.append((a, b))

num = 1
den = 1
for frac in fracs:
    num *= frac[0]
    den *= frac[1]

print(frac_reduce(num, den)[1])
