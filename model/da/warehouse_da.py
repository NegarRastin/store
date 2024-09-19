import mysql.connector

from warehouse import warehouse

class warehouseDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, warehouse):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into car_tbl (product,inventory) values (%s,%s)",
							[warehouse.product,warehouse.inventory])
		self.disconnect(commit = True)

	def edit(self, warehouse):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update car_tbl set  product=%s,inventory=%s  where id=%s",
							[warehouse.product,warehouse.inventory])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from car_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from car_tbl ")
		warehouse_list = [warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
		self.disconnect()
		if warehouse_list:
			return warehouse_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from car_tbl where id=%s", [id])
		warehouse = self.cursor.fetchone()
		self.disconnect()
		if warehouse:
			return warehouse(*warehouse)

