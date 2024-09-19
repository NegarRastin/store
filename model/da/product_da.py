import mysql.connector

class productDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, product):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into car_tbl (id,name,brand, model,price) values (%s,%s,%s,%s,%s)",
							[product.id,product.name,product.brand,product. model,product.price])
		self.disconnect(commit = True)

	def edit(self, product):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update car_tbl set name=%s,brand=%s, model=%s,price=%s    where id=%s",
							[product.name,product.brand,product. model,product.price,product.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from car_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from car_tbl ")
		product_list = [product(*product) for product in self.cursor.fetchall()]
		self.disconnect()
		if product_list:
			return product_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from car_tbl where id=%s", [id])
		product = self.cursor.fetchone()
		self.disconnect()
		if product:
			return product(*product)

