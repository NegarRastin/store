from model.entity.person import Person
from tools.validator import Validator


class Customer(Person):
    def __init__(self, id, name, family, national_code, phone_number):
        super().__init__(id, name, family, national_code)
        self.phone_number = phone_number

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = Validator.phone_number_validator(phone_number, "Invalid Phone Number")
