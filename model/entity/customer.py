import re
from model.entity.person import Person
# id, name, family, national_code, phone_number
class Customer(Person):
    def __init__(self, id, name, family, national_code, phone_number):
        self.id = id
        self.name = name
        self.family = family
        self.national_code=national_code
        self. phone_number=phone_number


    @property
    def national_code(self):
           return self._national_code

    @national_code.setter
    def national_code(self, value):
           if re.match(r"^[0-9/_]{10,12}$",value):
              self._national_code=value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
           if re.match(r"^(\+989\d{9}|09\d{9})$", value):
              self._phone_number=value
    def __repr__(self):
        return f"{self.__dict__}"
