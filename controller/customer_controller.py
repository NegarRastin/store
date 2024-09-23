from model.entity.customer import Customer
from model.da.customer_da import CustomerDa
from tools import exception_handling


class CustomerController:
    customer_da = CustomerDa()

    @classmethod
    @exception_handling
    def save(cls, name, family, national_code, phone_number):
        customer = Customer(0, name, family, national_code, phone_number)
        cls.customer_da.save(customer)
        return True, f"Customer {national_code} Saved"

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, national_code, phone_number):
        customer = Customer(id, name, family, national_code, phone_number)
        cls.customer_da.edit(customer)
        return True, f"Customer {national_code} Edited"

    @classmethod
    @exception_handling
    def remove(cls, id):
        cls.customer_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.customer_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.customer_da.find_by_id(id)
