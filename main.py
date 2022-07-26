# Write the function total_inventory, which takes two inventory dictionaries and a key and gives the total count of the item from both inventory lists. 

# Make sure it doesn’t produce an error if the item isn’t in the inventory lists (in this case assume the value is 0).

# Example

# Input
# -----
# inventory_0 = {"bananas": 2}
# inventory_1 = {"bananas": 5, "apples": 3}
# item = "bananas"

# Output
# ------
# 7



# Make sure to test on additional examples!
inventory_0 = {"bananas": 2}
inventory_1 = {"bananas": 5, "apples": 3, "pineapples": 2}
item = "pineapples"


def total_inventory(inventory_0, inventory_1, item):
  count = 0
  if item not in inventory_0 and item not in inventory_1:
    return 0
  elif item in inventory_0 and item not in inventory_1:
    count = inventory_0[item]
    return count
  elif item not in inventory_0 and item in inventory_1:
    count = inventory_1[item]
    return count
  else:
    count = inventory_0[item] + inventory_1[item]
    return count

print('Inventory Count:', total_inventory(inventory_0, inventory_1, item))