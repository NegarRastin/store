import mysql.connector



class customerDa:

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
		#todo : complete sql command and parameters
		self.cursor.execute("insert into car_tbl (id,nam,family, national_code, phone_number) values (%s,%s,%s,%s,%s,)",
							[  customer.id, customer.name,customer.family,customer.national_code,customer.phone_number])
		self.disconnect(commit = True)

	def edit(self, customer):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update car_tbl set   name=%s, family=%s, national_code=%s, phone_number=%s  where id=%s"
							[customer.name,customer.family,customer.national_code,customer.phone_number,customer.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from car_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from car_tbl ")
		customer_list = [customer(*customer) for customer in self.cursor.fetchall()]
		self.disconnect()
		if customer_list:
			return customer_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from car_tbl where id=%s", [id])
		customer = self.cursor.fetchone()
		self.disconnect()
		if customer:
			return customer(*customer)

