def divider(number):
    return number / 100

def changeCalculator2(amount, i):
     # Convert amount to cents
     # $100,$50,$10,$5,$2,$1, 50c,20c,10c,5c,1c
    coins = [10000,5000,1000,500,200, 100, 50, 20, 10, 5, 1]
    listOfCoins = []
    if amount == 0 or i == len(coins):
        return listOfCoins

    if coins[i] <= amount:
        # configure 1/ number = number
        remainder = amount - coins[i]
       # print(remainder)
        listOfCoins.extend([coins[i]])
        listOfCoins.extend(changeCalculator2(remainder, i))

    elif coins[i] > amount:
        remainder = amount  # Use amount instead of undefined remainder
        listOfCoins.extend(changeCalculator2(remainder, i + 1))
    return listOfCoins

# Example usage
amount = float(input("Please enter the amount you want in change : $"))
usedAmount = amount * 100
coins_in_cents = changeCalculator2(usedAmount, 0)
coins_in_dollars = list(map(divider, coins_in_cents))
print(coins_in_dollars)

