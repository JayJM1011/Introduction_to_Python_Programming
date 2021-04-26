prices= {'Bananas': 45, 'Apple': 200, 'Orange': 150,  'Pear': 120}
stock= {'Bananas': 6, 'Apple': 0, 'Orange': 32,  'Pear': 15}
for i in prices:
    print(i)
    print('Prices:', prices[i])
    print('Stock:', stock[i])
    print()
total= 0
for i in prices:
    total= total+ (prices[i]* stock[i])
print('The total is', total)