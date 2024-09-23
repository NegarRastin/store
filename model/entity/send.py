import re

from tools.validator import Validator


class Send:
    def __init__(self, id, product, quantity, customer, phone_number, address):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.customer = customer
        self.phone_number = phone_number
        self.address = address

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = Validator.id_validator(id, "Invalid Id")

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if re.match(r"^[0-9]{1,}$", quantity):
            self._quantity = quantity

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if re.match(r"^(\+989\d{9}|09\d{9})$", phone_number):
            self._phone_number = phone_number

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if re.match(r"[a-zA-z0-9,\-\s]{3,30}", address):
            self._address = address

    def __repr__(self):
        return f"{self.__dict__}"
