
from model.entity.customer import Customer
from model.da.customer_da import customerDa


class customerController:
    customer_da = customerDa()

    @classmethod
    def save(cls, id, name, family, national_code, phone_number):
        try:
            customer = Customer(id, name, family, national_code, phone_number)
            cls.customer_da.save(customer)
            return True, f"Customer {national_code} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls,id, name, family, national_code, phone_number ):
        try:
            customer = Customer(id, name, family, national_code, phone_number)
            cls.customer_da.edit(customer)
            return True, f"Customer {national_code} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, national_code):
        try:
            cls.customer_da.remove(national_code)
            return True, f"Customer {national_code} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.customer_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, cls.customer_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

