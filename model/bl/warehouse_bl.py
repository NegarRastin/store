from model.da.warehouse_da import warehouseDa
from model.entity.product import Product



class WarehouseBl:
    @staticmethod
    def save(warehouse):
        sell_da =warehouseDa()
        return sell_da.save(warehouse)

    @staticmethod
    def edit(warehouse):
        customer_da = warehouseDa()
        return customer_da.edit(warehouse)

    @staticmethod
    def remove(warehouse):
        sell_da = warehouseDa()
        return sell_da.remove(warehouse)

    @staticmethod
    def find_all(warehouse):
        customer_da = warehouseDa()
        return customer_da.find_all(warehouse)

    @staticmethod
    def find_by_id (warehouse):
        sell_da = warehouseDa()
        return sell_da.find_by_id(warehouse)