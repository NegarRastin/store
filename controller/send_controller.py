from model.entity.send import Send
from model.da.send_da  import sendDa


class sendController:
    send_da = sendDa()

    @classmethod
    def save(cls, product, quantity, customer, phone_number, address):
        try:
            send = Send(product, quantity, customer, phone_number, address)
            cls.send_da.save(send)
            return True, f"send {customer} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls,product, quantity, customer, phone_number, address ):
        try:
            send = Send(product, quantity, customer, phone_number, address)
            cls.send_da.edit(send)
            return True, f"send {customer} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, customer):
        try:
            cls.send_da.remove(id)
            return True, f"send {customer} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.send_da.find_all()
        except Exception as e:
            return False, str(e)


