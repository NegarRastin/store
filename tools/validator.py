import re
from datetime import datetime,date


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def family_validator(cls, family, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", family):
            return family
        else:
            raise ValueError(message)


    @classmethod
    def id_validator(cls, id, message):
        if re.match(r"^[0-9]{1,}$", id):
            return id
        else:
            raise ValueError(message)



    @classmethod
    def national_validator(cls, national_code, message):
        if re.match(r"^[0-9/_]{10,12}$",  national_code):
            return national_code
        else:
            raise ValueError(message)

    @classmethod
    def phone_number_validator(cls, phone_number, message):
        if re.match(r"^(\+989\d{9}|09\d{9})$",phone_number ):
            return phone_number
        else:
            raise ValueError(message)

    @classmethod
    def brand_validator(cls,brand , message):
        if re.match(r"^[a-zA-Z\s]{3,30}$",brand ):
            return brand
        else:
            raise ValueError(message)

    @classmethod
    def model_validator(cls, model, message):
        if re.match(r"^[a-zA-Z0-9\s]{3,30}$", model):
            return model
        else:
            raise ValueError(message)

    @classmethod
    def price_validator(cls, price, message):
        if re.match(r"^[0-9]{2,30}$", price):
            return price
        else:
            raise ValueError(message)


    @classmethod
    def customer_validator(cls, customer, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", customer):
            return customer
        else:
            raise ValueError(message)


    def product_validator(cls, product, message):
        if re.match(r"^[a-zA-Z\s]{3,30}$", product):
            return product
        else:
            raise ValueError(message)

    def quantity_validator(cls, quantity, message):
        if re.match(r"^[0-9]{1,}$", quantity):
            return quantity
        else:
            raise ValueError(message)

    def address_validator(cls, address, message):
        if re.match(r"[a-zA-z0-9,\-\s]{3,30}", address):
            return address
        else:
            raise ValueError(message)









