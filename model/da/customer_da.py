import mysql.connector

from model.entity.customer import Customer


class CustomerDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "insert into customer_tbl (name, family, national_code, phone_number) values (%s,%s,%s,%s)",
            [customer.name, customer.family, customer.national_code, customer.phone_number])
        self.disconnect(commit=True)

    def edit(self, customer):
        self.connect()
        self.cursor.execute(
            "update customer_tbl set name=%s, family=%s, national_code=%s, phone_number=%s where id=%s",
            [customer.name, customer.family, customer.national_code, customer.phone_number, customer.id])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from customer_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from customer_tbl ")
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        if customer_list:
            return customer_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from customer_tbl where id=%s", [id])
        customer = self.cursor.fetchone()
        self.disconnect()
        if customer:
            return Customer(*customer)
