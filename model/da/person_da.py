import mysql.connector



class personDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, person):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into car_tbl (id,name,family) values (%s,%S,%s)",
							[person.id,person.name,person.famiLy])
		self.disconnect(commit = True)

	def edit(self, person):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update car_tbl set name=%S,family=%s   where id=%s",[person.name,person.famiLy,person.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from car_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from car_tbl ")
		person_list = [person(*person) for person in self.cursor.fetchall()]
		self.disconnect()
		if person_list:
			return person_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from car_tbl where id=%s", [id])
		person = self.cursor.fetchone()
		self.disconnect()
		if person:
			return person(*person)

