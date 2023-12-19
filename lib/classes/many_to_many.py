class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        coffee_orders = [] #array with relevant orders
        for order in Order.all:
            if(order.coffee == self):
                coffee_orders.append(order)
        return coffee_orders
    
    def customers(self):
        # the element that we want in the array - customer
        # for loop - orders
        # if statement
        # list(set()) = to get UNIQUE COFFEE OBJECTS!!!!
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        #sum of all prices of orders (self.orders())
        #number of orders (self.num_orders())
        # for loop method
        # total = 0
        # for order in self.orders():
        #     total += order.price
        # return total/self.num_orders()
        # list comprehension
        total = sum([order.price for order in self.orders()])
        return total/self.num_orders()
    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name
        
    @name.setter
    def name(self, val):
        if not hasattr(self, 'name') and isinstance(val, str) and len(val) >= 3:
            self._name = val

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        # list comprehension = need orders, iterate over Orders.all
        # if order.customer == self
        return [order for order in Order.all if order.customer == self]

    
    def coffees(self):
        # get all customer's coffees
        # list(set()) = to get UNIQUE COFFEE OBJECTS!!!!
        customer_coffees = []
        for order in self.orders():
            customer_coffees.append(order.coffee)
        return list(set(customer_coffees))

    
    def create_order(self, coffee, price):
        new_order = Order(price = price, customer = self, coffee = coffee)
        return new_order
    
    @property
    def name(self):
        return self._name
    
    @name.getter
    def name(self):
        return self._name
    
    @name.setter
    def name (self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val


class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.getter
    def price(self):
        return self._price
    
    @price.setter
    # ERROR WITH price is immutable - assert 3.0 == 2.0 (Need to add "not" to and not hasattr)
    def price(self, val):
        if isinstance(val, float) and 1.0 <= val <= 10.0 and not hasattr(self, 'price'):
            self._price = val