# Three people denoted by P1, P2, P3 intended to buy some rolls, buns, cakes and bread.
# Each of them needs these commodities in differing amounts 
# and can buy them in two shops S1, S2
# Which shop is the best for every person P1, P2, P3 to pay as little as possible? 
# The individual prices and desired quantities of the commodities are given
# Demanded quantity of foodstuff
# Prices in shops S1 and S2 

import numpy as np

# Demanded quantity of foodstuff for each person
demands = np.array([[6, 5, 3, 1],
                    [3, 6, 2, 2],
                    [3, 4, 3, 1]])

# Prices in shops S1 and S2
prices = np.array([[1.50, 1.00],
                   [2.00, 2.50],
                   [5.00, 4.50],
                   [16.00, 17.00]])

# Calculate total cost for each shop for each person
total_cost_S1 = np.sum(demands * prices[:, 0], axis=1)
total_cost_S2 = np.sum(demands * prices[:, 1], axis=1)

# Determine the best shop for each person
best_shops = np.where(total_cost_S1 < total_cost_S2, 'S1', 'S2')

print(total_cost_S1)
print(total_cost_S2)

# Output the result
for i, person in enumerate(['P1', 'P2', 'P3']):
    print(f"For person {person}, the best shop is {best_shops[i]}")
