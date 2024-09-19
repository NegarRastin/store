from model.da.product_da import productDa
from model.entity.product import Product

class ProductBl:
    @staticmethod
    def save(product):
        customer_da = productDa()
        return customer_da.save(product)

    @staticmethod
    def edit(product):
        customer_da = productDa()
        return customer_da.edit(product)

    @staticmethod
    def remove(product):
        customer_da = productDa()
        return customer_da.remove(product)

    @staticmethod
    def find_all(product):
        customer_da = productDa()
        return customer_da.find_all(product)

    @staticmethod
    def find_by_id (product):
        customer_da = productDa()
        return customer_da.find_by_id(product)