# Project Euler
# Alex Johnson
# Problem 31: Coin sums

coins = [1, 2, 5, 10, 20, 50, 100, 200]
value = 200

def poss(val, coin): return val // coin

def combos(val, ci):
    if val == 0: return 1
    if ci < 0: return 0
    count = 0
    for i in range(poss(val, coins[ci]) + 1):
        count += combos(val - (coins[ci] * i), ci - 1)
    return count

print(combos(value, len(coins) - 1))
