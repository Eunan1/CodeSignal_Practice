fruit_basket = {'appled': 5, 'banannas': 4, 'oranges': 8}

# Obtain the total number of fruit in the basket (Sum of Value)
total_fruits = sum(fruit_basket.values())
print(total_fruits)

# Obtain the total number of unique fruits in the basket (Sum of Keys)
count_fruits = len(fruit_basket)
print(count_fruits)

# Obtain which fruit has the lowest value in the basket
min_fruit = min(fruit_basket, key=fruit_basket.get)
print(min_fruit)

# Obtain which fruit has the highest vakue in the basket
max_fruit = max(fruit_basket, key=fruit_basket.get)
print(max_fruit)

# Obtain the average number of each distict type of fruit
avg_fruit = sum(fruit_basket.values()) / len(fruit_basket)
print(avg_fruit)