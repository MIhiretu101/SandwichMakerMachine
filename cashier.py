class Cashier:
    def __init__(self):
        pass

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