import re

from tools.validator import Validator


class Product:
    def __int__(self, id, name, brand, model, price):
        self.id = id
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = Validator.id_validator(id, "Invalid Id")

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[a-zA-Z\s]{3,30}$", name):
            self._name = name

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if re.match(r"^[a-zA-Z\s]{3,30}$", brand):
            self._brand = brand

    # model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if re.match(r"^[a-zA-Z0-9\s]{3,30}$", model):
            self._model = model

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if re.match(r"^[0-9]{2,30}$", price):
            self._price = price

    def __repr__(self):
        return f"{self.__dict__}"
