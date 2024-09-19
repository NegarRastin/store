from model.entity.product import Product
from model.da.product_da  import productDa


class productController:
    product_da = productDa()

    @classmethod
    def save(cls, id,name,brand, model,price):
        try:
            product = Product(id,name,brand, model,price)
            cls.product_da.save(product)
            return True, f"product {name} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls,id,name,brand, model,price ):
        try:
            product = Product(id,name,brand, model,price)
            cls.product_da.edit(product)
            return True, f"product {id} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            cls.product_da.remove(id)
            return True, f"Product {id} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.product_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, cls.product_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

