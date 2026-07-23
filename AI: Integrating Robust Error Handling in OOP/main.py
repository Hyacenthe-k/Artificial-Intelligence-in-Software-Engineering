# 1. Define the custom exception
class InvalidProductDataError(Exception):
    """Custom exception for invalid product data."""
    def __init__(self, message):
        super().__init__(message)

# 2. Refactor the Product class with properties and validation
class Product:
    """Represents a product with validated price and quantity."""
    def __init__(self, name, price, quantity):
        self.name = name
        # These assignments now call the setter methods
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """Gets the product's price."""
        return self._price

    @price.setter
    def price(self, value):
        """Sets the product's price with validation."""
        if not isinstance(value, (int, float)):
            raise InvalidProductDataError(
                f"Invalid type for price. Expected int or float, but got {type(value).__name__}."
            )
        if value < 0:
            raise InvalidProductDataError(
                f"Invalid value for price. Price cannot be negative, but got {value}."
            )
        self._price = value

    @property
    def quantity(self):
        """Gets the product's quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Sets the product's quantity with validation."""
        if not isinstance(value, int):
            raise InvalidProductDataError(
                f"Invalid type for quantity. Expected int, but got {type(value).__name__}."
            )
        if value < 0:
            raise InvalidProductDataError(
                f"Invalid value for quantity. Quantity cannot be negative, but got {value}."
            )
        self._quantity = value

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

# 3. Inventory Manager remains compatible
class InventoryManager:
    """Manages a collection of products in inventory."""
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        if product.name in self.inventory:
            self.inventory[product.name].quantity += product.quantity
        else:
            self.inventory[product.name] = product
        print(f"Added/updated product: {product.name}")

    def get_inventory_value(self):
        total_value = 0
        for product in self.inventory.values():
            total_value += product.price * product.quantity
        return total_value

# 4. Demonstration of the new implementation
if __name__ == "__main__":
    manager = InventoryManager()
    
    print("--- Testing Valid Data ---")
    try:
        laptop = Product("Laptop", 1200.50, 10)
        manager.add_product(laptop)
        print(f"Successfully created: {laptop}")
        laptop.quantity = 15
        print(f"Successfully updated quantity: {laptop.quantity}")
    except InvalidProductDataError as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- Testing Invalid Input ---")
    try:
        laptop.quantity = -5
    except InvalidProductDataError as e:
        print(f"Test result: {e}")

    print(f"\nCurrent Inventory Value: ${manager.get_inventory_value():.2f}")
