

def MathChallenge(num: int):
    coins = [1, 5, 7, 9, 11]
    used_coins = []
    total = num

    for i in reversed(coins):
        while i <= total:
            total = total - i

            used_coins.append(i)

            if total == 0:
                #return len(used_coins)
                return used_coins


print(MathChallenge(25))
