from model.da.customer_da import customerDa
from model.entity.customer import Customer

class CustomerBl:
    @staticmethod
    def save(customer):
        customer_da = customerDa()
        return customer_da.save(customer)

    @staticmethod
    def edit(customer):
        customer_da = customerDa()
        return customer_da.edit(customer)

    @staticmethod
    def remove(customer):
        customer_da = customerDa()
        return customer_da.remove(customer)

    @staticmethod
    def find_all(customer):
        customer_da = customerDa()
        return customer_da.find_all(customer)

    @staticmethod
    def find_by_id (customer):
        customer_da = customerDa()
        return customer_da.find_by_id(customer)