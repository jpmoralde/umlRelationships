class Order:
    pass
class Customer:
    def __init__(self, order):
        self.order = order
order = Order()
customer = Customer(order)
print(customer.order)