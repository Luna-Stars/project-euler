# Project Euler
# Alex Johnson
# Problem 37: Truncatable primes

def truncate_left(x):
    truncated = []
    for i in range(1, len(str(x))):
        truncated.append(int(str(x)[i:]))
    truncated.sort()
    return truncated

def truncate_right(x):
    truncated = []
    for i in range(1, len(str(x))):
        truncated.append(int(str(x)[:-i]))
    truncated.sort()
    return truncated

sieve = list(range(2, 2000000))

for i in range(len(sieve)):
    key = sieve[i]
    if key != -1:
        j = i + key
        while j < len(sieve):
            sieve[j] = -1
            j += key

sieve = [x for x in sieve if x != -1]

count = 0
total = 0
i = 10

for i in sieve:
    if count == 11: break
    if i < 10: continue
    l = truncate_left(i)+truncate_right(i)
    isValid = True
    for x in l:
        if x not in sieve:
            isValid = False
            break
    if isValid:
        print("found #"+str(count + 1)+": "+str(i)+". current total: "+str(total + i))
        count += 1
        total += i

print(total)
