import re
from datetime import datetime

# id, customer, product, count, price, date_time
class Sell:
    def __int__(self,id, customer, product, quantity, price ):
        self.id= id
        self.customer  = customer
        self.product = product
        self.quantity= quantity
        self.price = price
        self.date_time=datetime.now()

        @property
        def id(self):
           return self._id

        @id.setter
        def id(self, value):
            if re.match(r"^[1-9]{1,}$", value):
                self._id = value


        @property
        def customer(self):
            return self._customer

        @customer.setter
        def customer(self, value):
            if re.match(r"^[a-zA-Z\s]{3,30}$", value):
               self._customer=value

        @property
        def product(self):
            return self._product

        @product.setter
        def product(self, value):
            if re.match(r"^[a-zA-Z\s]{3,30}$", value):
               self._product=value


        @property
        def quantity(self):
            return self._quantity

        @quantity.setter
        def quantity(self, value):
            if re.match(r"^[0-9]{1,}$", value):
               self._quantity=value




        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
                if re.match(r"^[0-9]{3,30}$", value):
                    self._price = value

    def __repr__(self):
              return f"{self.__dict__}"



