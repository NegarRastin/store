import mysql.connector



class sendDa:

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
		#todo : complete sql command and parameters
		self.cursor.execute("insert into car_tbl ( product, quantity, customer, phone_number, address values (%s,%s,%s,%s,%s)",
							[send.product, send.quantity, send.customer, send.phone_number, send.address])
		self.disconnect(commit = True)

	def edit(self, send):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update car_tbl set  product=%s, quantity=%s, customer=%s, phone_number=%s, address=%s   where id=%s",
							[send.product, send.quantity, send.customer, send.phone_number, send.address])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from car_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from car_tbl ")
		send_list = [send(*send) for send in self.cursor.fetchall()]
		self.disconnect()
		if send_list:
			return send_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from send_tbl where id=%s", [id])
		send = self.cursor.fetchone()
		self.disconnect()
		if send:
			return send(*send)

