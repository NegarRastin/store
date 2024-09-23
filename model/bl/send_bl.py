from model.da.send_da import SendDa
from model.entity.product import Product



class SendBl:
    @staticmethod
    def save(send):
        sell_da = send()
        return sell_da.save(send)

    @staticmethod
    def edit(send):
        customer_da = send()
        return customer_da.edit(send)

    @staticmethod
    def remove(send):
        sell_da = SendDa()
        return sell_da.remove(send)

    @staticmethod
    def find_all(send):
        send_da = SendDa()
        return send_da.find_all(send)

