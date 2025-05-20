class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        if not (isinstance(price, float) or isinstance(price, int)) or not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price