import mysql.connector

from model.entity.send import Send


class SendDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, send):
        self.connect()
        self.cursor.execute(
            "insert into send_tbl ( product_id, quantity, customer_id, phone_number, address) values (%s,%s,%s,%s,%s)",
            [send.product.id, send.quantity, send.customer.id, send.phone_number, send.address])
        self.disconnect(commit=True)

    def edit(self, send):
        self.connect()
        self.cursor.execute(
            "update send_tbl set  product_id=%s, quantity=%s, customer_id=%s, phone_number=%s, address=%s where id=%s",
            [send.product.id, send.quantity, send.customer.id, send.phone_number, send.address, send.id])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from send_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from send_tbl ")
        send_list = [Send(*send) for send in self.cursor.fetchall()]
        self.disconnect()
        if send_list:
            return send_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from send_tbl where id=%s", [id])
        send = self.cursor.fetchone()
        self.disconnect()
        if send:
            return Send(*send)
