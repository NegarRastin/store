import re


class Product:
    def __int__(self, name, model, price, id):
        self.name = name
        self.model = model
        self.price = price
        self.id = id
       #name
        @property
        def name(self):
            if re.match(r"^[a-zA-Z\s]{3,30}$", self.name):
                return self._name


        @name.setter
        def name(self, value):
            if re.match(r"^[a-zA-Z\s]{3,30}$", value):
                self._name=value

            @property
            def price(self):
                if re.match(r"^[1-9]{3,30}$", self.price):
                    return self._price

            @price.setter
            def id(self, value):
                if re.match(r"^[1-9]{3,30}$", value):
                    self._id = value


            #id
        @property
        def id(self):
            if re.match(r"^[1-9]{1}$", self.id):
               return self._id

        @id.setter
        def id(self, value):
            if re.match(r"^[1-9]{1}$", value):
               self._id =value
            #model
        @property
        def modeL (self):
            if re.match(r"^[a-zA-Z0-9\s]{3,30}$", self.model):
               return self._model

        @model.setter
        def model(self, value):
            if re.match(r"^[a-zA-Z0-9\s]{3,30}$", self.model):
               self._model=value

