from model.da.sell_da import sellDa




class SellBl:
    @staticmethod
    def save(sell):
        sell_da = sellDa()
        return sell_da.save(sell)

    @staticmethod
    def edit(sell):
        customer_da = sellDa()
        return customer_da.edit(sell)

    @staticmethod
    def remove(sell):
        sell_da = sellDa()
        return sell_da.remove(sell)

    @staticmethod
    def find_all(sell):
        customer_da = sellDa()
        return customer_da.find_all(sell)

    @staticmethod
    def find_by_id (sell):
        sell_da = sellDa()
        return sell_da.find_by_id(sell)