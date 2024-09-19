import mysql.connector


class sellDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, sell):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into car_tbl (id, customer, product, quantity, price,date_time) values (%s,%s,%s,%s,%s,%s)",
							[sell.id, sell.customer, sell.product, sell.quantity, sell.price,sell.date_time])
		self.disconnect(commit = True)

	def edit(self, sell):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update car_tbl set  customer=%s, product=%s, quantity=%s, price=%s,date_time=%s   where id=%s",
							[ sell.customer, sell.producl, sell.quantity, sell.price,sell.date_time,sell.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from car_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from car_tbl ")
		sell_list = [sell(*sell) for sell in self.cursor.fetchall()]
		self.disconnect()
		if sell_list:
			return sell_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from car_tbl where id=%s", [id])
		sell = self.cursor.fetchone()
		self.disconnect()
		if sell:
			return sell(*sell)

