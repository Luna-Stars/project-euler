# Project Euler
# Alex Johnson
# Problem 29: Distinct powers

terms = []

for a in range(2, 101):
    for b in range(2, 101):
        val = a**b
        if val not in terms: terms.append(val)

print(len(terms))
