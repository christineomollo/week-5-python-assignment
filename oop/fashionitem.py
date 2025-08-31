# Base class for fashion items
class FashionItem:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self._price = price  # encapsulated attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative.")
        self._price = value

    def describe(self):
        return f"{self.name} by {self.brand} - ${self.price:.2f}"


# Subclass for clothing items
class Clothing(FashionItem):
    def __init__(self, name, brand, price, size, material):
        super().__init__(name, brand, price)
        self.size = size
        self.material = material

    def describe(self):
        return f"Clothing: {self.name} ({self.size}, {self.material}) by {self.brand} - ${self.price:.2f}"


# Subclass for accessories
class Accessory(FashionItem):
    def __init__(self, name, brand, price, accessory_type):
        super().__init__(name, brand, price)
        self.accessory_type = accessory_type

    def describe(self):
        return f"Accessory: {self.accessory_type} - {self.name} by {self.brand} - ${self.price:.2f}"


# Subclass for footwear
class Footwear(FashionItem):
    def __init__(self, name, brand, price, size, style):
        super().__init__(name, brand, price)
        self.size = size
        self.style = style

    def describe(self):
        return f"Footwear: {self.style} {self.name} (Size {self.size}) by {self.brand} - ${self.price:.2f}"


# The Fashion Boutique class managing inventory
class FashionBoutique:
    def __init__(self, boutique_name, owner):
        self.boutique_name = boutique_name
        self.owner = owner
        self.inventory = []

    def add_item(self, item: FashionItem):
        self.inventory.append(item)
        print(f"Added {item.name} to {self.boutique_name}'s inventory.")

    def list_inventory(self):
        if not self.inventory:
            print(f"{self.boutique_name} has no items currently.")
            return
        print(f"Inventory of {self.boutique_name}:")
        for item in self.inventory:
            print(" - " + item.describe())

    def total_value(self):
        return sum(item.price for item in self.inventory)
