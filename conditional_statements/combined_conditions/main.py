# The item's discount and stock status have been defined
discounted = False
lowStock = True

movingProduct = lowStock or discounted
promotion = discounted and not lowStock
print(f"Is the item eligible for promotion? {promotion}")


