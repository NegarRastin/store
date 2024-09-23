import re


class Person:
    def __init__(self, id, name, family):
        self.id = id
        self.name = name
        self.family = family

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if re.match(r"^[0-9]{1,}$", value):
            self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"^[a-zA-Z\s]{3,30}$", value):
            self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        if re.match(r"^[a-zA-Z\s]{3,30}$", value):
            self._family = value
