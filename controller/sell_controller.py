from model.entity.sell import Sell
from model.da.sell_da  import sellDa


class sellController:
    sell_da = sellDa()

    @classmethod
    def save(cls, id, customer, product, quantity, price):
        try:
            sell = Sell(id, customer, product, quantity, price)
            cls.sell_da.save(sell)
            return True, f"sell {product} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls,id, customer, product, quantity, price ):
        try:
            sell = Sell(id, customer, product, quantity, price)
            cls.sell_da.edit(sell)
            return True, f"sell {id} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            cls.sell_da.remove(id)
            return True, f"Product {id} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.sell_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, cls.sell_da.find_by_id(id)
        except Exception as e:
            return False, str(e)

