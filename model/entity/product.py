import re

# id, name,brand, model, price
class Product:
    def __int__(self,id,name,brand, model,price):
        self.id = id
        self.name = name
        self.brand=brand
        self.model = model
        self.price = price

        # id
        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            if re.match(r"^[0-9]{1,}$", value):
                self._id = value

       #name
        @property
        def name(self):
             return self._name


        @name.setter
        def name(self, value):
            if re.match(r"^[a-zA-Z\s]{3,30}$", value):
                self._name = value

        @property
        def brand(self):
            return self._brand

        @brand.setter
        def brand(self, value):
                if re.match(r"^[a-zA-Z\s]{3,30}$",value):
                   self._brand=value

            #model
        @property
        def modeL (self):
            return self._model

        @model.setter
        def model(self, value):
            if re.match(r"^[a-zA-Z0-9\s]{3,30}$", self.model):
               self._model=value

        @property
        def price(self):
            return self._price

        @price.setter
        def prie(self, value):
            if re.match(r"^[0-9]{2,30}$", value) :
                self._price= value

    def __repr__(self):
        return f"{self.__dict__}"
