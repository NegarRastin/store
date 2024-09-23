from model.da.customer_da import CustomerDa
from model.entity.customer import Customer


class CustomerBl:

    @staticmethod
    def save(customer):
        customer_da = CustomerDa()
        customer_da.save(customer)

    @staticmethod
    def edit(customer):
        customer_da = CustomerDa()
        customer_da.edit(customer)

    @staticmethod
    def remove(id):
        customer_da = CustomerDa()
        customer_da.remove(id)

    @staticmethod
    def find_all():
        customer_da = CustomerDa()
        return customer_da.find_all()

    @staticmethod
    def find_by_id(id):
        customer_da = CustomerDa()
        return customer_da.find_by_id(id)
