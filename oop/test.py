# Create boutique
boutique = FashionBoutique("Chic Styles", "Sophia")

# Create products
shirt = Clothing("Silk Shirt", "Gucci", 250.0, "M", "Silk")
watch = Accessory("Classic Watch", "Rolex", 12000.0, "Watch")
sneakers = Footwear("Air Max", "Nike", 150.0, 42, "Running")

# Add products to boutique
boutique.add_item(shirt)
boutique.add_item(watch)
boutique.add_item(sneakers)

# List all items
boutique.list_inventory()

# Show total inventory value
print(f"Total inventory value: ${boutique.total_value():.2f}")
