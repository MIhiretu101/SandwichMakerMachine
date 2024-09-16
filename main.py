### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """
        Checks if the machine has enough resources to make the sandwich.
        Returns True if ingredients are sufficient, otherwise False.
        """
        for item, quantity in ingredients.items():
            if self.machine_resources[item] < quantity:
                return False
        return True

    def process_coins(self):
        """
        Returns the total value of coins inserted by the user as a float.
        """
        print("\nPlease insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        total = (large_dollars * 1) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return float(total)

    def transaction_result(self, coins, cost):
        """
        Returns True if the payment is accepted, or False if money is insufficient.
        If accepted, it also returns the change.
        """
        if coins >= cost:
            return True, coins - cost  # Transaction successful, return True and change
        else:
            return False, -1  # Transaction failed, return False and no change

    def make_sandwich(self, sandwich_size, order_ingredients):
        """
        Deduct the required ingredients from the machine's resources.
        """
        for item, quantity in order_ingredients.items():
            self.machine_resources[item] -= quantity


### Main program ###

machine = SandwichMachine(resources)

while True:
    print("\nWhat would you like? (small/ medium/ large/ off/ report): ")
    order = input().lower()

    if order == "off":
        print("Turning off the machine. Goodbye!")
        break

    elif order == "report":
        print("\nResources report:")
        for item, quantity in machine.machine_resources.items():
            print(f"{item.capitalize()}: {quantity} {'slice(s)' if item != 'cheese' else 'ounce(s)'}")

    elif order in recipes:
        order_ingredients = recipes[order]["ingredients"]
        if machine.check_resources(order_ingredients):
            coins = machine.process_coins()
            cost = recipes[order]["cost"]
            transaction_successful, change = machine.transaction_result(coins, cost)

            if transaction_successful:
                if change > 0:
                    print(f"\nHere is ${change:.2f} in change.")
                else:
                    print("\nNo change.")
                machine.make_sandwich(order, order_ingredients)
                print(f"\n{order.capitalize()} sandwich is ready. Bon appetit!")
            else:
                print("\nSorry, that's not enough money. Money refunded.")
        else:
            insufficient_ingredient = [
                item for item, quantity in order_ingredients.items()
                if machine.machine_resources[item] < quantity
            ][0]
            print(f"\nSorry, there is not enough {insufficient_ingredient}.")
    else:
        print("\nInvalid order. Please try again.")
