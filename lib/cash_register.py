#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize discount, total, and items
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Add the price * quantity to the total
        self.total += price * quantity
        # Record the items added
        self.items.extend([title] * quantity)
        # Keep track of the last transaction for voiding
        self.last_transaction = price * quantity

    def apply_discount(self):
        # Check if discount is available
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Print success message with the updated total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            # Print error message if no discount available
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract the last transaction amount from the total
        self.total -= self.last_transaction
        # Reset the last transaction amount
        self.last_transaction = 0

