# Project Euler
# Alex Johnson
# Problem 17: Number letter counts

import inflect
p = inflect.engine()

letters = ""

for i in range(1,1001):
    letters += p.number_to_words(i)

letters = letters.replace(" ", "").replace("-", "")
print(len(letters))
