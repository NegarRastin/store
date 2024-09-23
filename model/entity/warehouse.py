class Warehouse:
    def __init__(self,id, product, inventory):
        self.id = id
        self.product = product
        self.inventory = inventory


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id


    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        self._inventory = inventory

    def __repr__(self):
        return f"{self.__dict__}"
