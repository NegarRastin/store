import re

# id, name, family, national_code, phone_number
class Customer:
    def __init__(self, id, firstname, family):
        self.id = id
        self.firstname = firstname
        self.family = family

    @property
    def id(self):
        if re.match(r"^[1-9]{1}$", self.id):
            return self._id

    @id.setter
    def id(self, value):
        if re.match(r"^[1-9]{1}$", value):
            self._id = value

    @property
    def firstname(self):
       if re.match(r"^[a-zA-Z\s]{3,30}$", self.firstname):
          return self._firstname

    @firstname.setter
    def name(self, value):
        if re.match(r"^[a-zA-Z\s]{3,30}$", value):
           self._firstname = value

           @property
           def family(self):
               if re.match(r"^[a-zA-Z\s]{3,30}$", self.family):
                   return self._family

           @family.setter
           def family(self, value):
               if re.match(r"^[a-zA-Z\s]{3,30}$", value):
                  self._family = value
