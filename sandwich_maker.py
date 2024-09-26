class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """
        Checks if the machine has enough resources to make the sandwich.
        Returns True if ingredients are sufficient, otherwise False.
        """
        for item, quantity in ingredients.items():
            if self.machine_resources[item] < quantity:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """
        Deduct the required ingredients from the machine's resources.
        """
        for item, quantity in order_ingredients.items():
            self.machine_resources[item] -= quantity
