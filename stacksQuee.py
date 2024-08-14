
class RestaurantOrder:
    def __init__(self, customer, dishes, cost):
        self.customer = customer
        self.dishes = dishes
        self.cost = cost

    def __str__(self):
        order = f"Customer: {self.customer}\nOrder:"
        for i in range(len(self.dishes)):
            order += f"\n    {self.dishes[i]}"
        order += f"\nOrder Total: ${self.cost}"
        return order
    
    def notify_customer(self):
        print(f"{self.customer}, your order is ready!\n")

class OrderQueue:
    def __init__(self):
        self.orders = []

    def is_empty(self):
        return len(self.orders) == 0

    def add_new_order(self, order):
        self.orders.append(order)

    def complete_next_order(self):
        if not self.is_empty():
            print("Order up!")
            order = self.orders.pop(0)
            print(f"{order}")
            order.notify_customer()
        else:
            print("All orders have been fulfilled! Clean some dishes!")

lunch_rush = OrderQueue()

lunch_rush.add_new_order(RestaurantOrder(
    "James",
    ["2 x Double Cheeseburger",
     "1 x Lg Fries",
     "1 x Hazy IPA",
     "1 x Kolsch"
     ],
     "52.48"))
lunch_rush.add_new_order(RestaurantOrder(
    "Wendell",
    ["1 x Cheeseburger",
     "1 x Sm Fries",
     "1 x Sm Soda"
     ],
     "14.82"))
lunch_rush.add_new_order(RestaurantOrder(
    "Arielle",
    ["1 x Burrito",
     "1 x Cheese Fries",
     "1 x Margarita"
     ],
     "23.97"))

lunch_rush.complete_next_order()

lunch_rush.add_new_order(RestaurantOrder(
    "Chris",
    ["2 x Double Cheeseburger",
     "1 x Cheese Fries",
     "1 x Stout",
     "1 x Aviation"
     ],
     "57.33"))

lunch_rush.complete_next_order()
lunch_rush.complete_next_order()

lunch_rush.add_new_order(RestaurantOrder(
    "Peach",
    ["1 x Md Fries"],
     "5.19"))

lunch_rush.complete_next_order()
lunch_rush.complete_next_order()
lunch_rush.complete_next_order()