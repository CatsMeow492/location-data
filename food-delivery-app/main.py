class FoodDelivery:
    def __init__(self, number, items):
        self.number = number
        self.items = items

    def submit_order(self, items):
        print(f"Submittinng order: {self.number}")

    def make_food(self, item):
        print(f"Made {item}")

    def package_item(self, item):
        print(f"Packaging {item}")

    def complete_order(self):
        self.submit_order()
        for i in self.items:
            self.make_food(i)
            self.package_item(i)
        print("Delivering order", self.number)

myOrder = FoodDelivery(123, "Ramen")
myOrder.complete_order()