
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    machine = SandwichMachine(resources, sandwich_maker_instance, cashier_instance)

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


class SandwichMachine:

    def __init__(self, machine_resources, sandwich_maker, cashier):
        """Receives resources as input."""
        self.machine_resources = machine_resources
        self.sandwich_maker = sandwich_maker
        self.cashier = cashier

    def check_resources(self, order_ingredients):
        return self.sandwich_maker.check_resources(order_ingredients)

    def process_coins(self):
        return self.cashier.process_coins()

    def transaction_result(self, coins, cost):
        return self.cashier.transaction_result(coins, cost)

    def make_sandwich(self, order, order_ingredients):
        self.sandwich_maker.make_sandwich(order, order_ingredients)


if __name__ == "__main__":
    main()
