from tools.validator import Validator


class Person:
    def __init__(self, id, name, family, national_code):
        self.id = id
        self.name = name
        self.family = family
        self.national_code = national_code

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = Validator.id_validator(id, "Invalid Id")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = Validator.family_validator(value, "Invalid Family")

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, national_code):
        self._national_code = Validator.national_validator(national_code, "Invalid National Code")

    def __repr__(self):
        return f"{self.__dict__}"
