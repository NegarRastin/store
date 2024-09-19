import re
class Warehouse:
	def __init__(self, product, inventory):
		self.product = product
		self.inventory = inventory

	@property
	def product(self):
		return self._product

	@product.setter
	def product(self, product):
		if re.match(r"^[a-zA-Z\s]{3,30}$", product):
			self._product = product

	@property
	def inventory(self):
		return self._inventory

	@inventory.setter
	def inventory(self, inventory):
		#todo : Add Validator
		self._inventory = inventory

	def __repr__(self):
		return f"{self.__dict__}"
