def total_inventory(inventory_0, inventory_1, item):
    count = inventory_0.get(item, 0)
    count += inventory_1.get(item, 0)
    return count


print(total_inventory({"bananas": 2}, {"bananas": 5, "apples": 3}, "bananas"))

print(total_inventory({"bananas": 2}, {"bananas": 5, "apples": 3}, "carrots"))

print(total_inventory({"bananas": 2}, {"bananas": 5, "apples": 3}, "apples"))
