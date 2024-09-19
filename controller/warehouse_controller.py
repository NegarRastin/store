from model.entity.warehouse import Warehouse
from model.da.warehouse_da import warehouseDa


class warehouseController:
   warehouse_da = warehouseDa()

    @classmethod
    def save(cls,product,inventory):
        try:
            warehouse = Warehouse(product,inventory)
            cls.warehouse_da.save(warehouse)
            return True, f"warehouse {product} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, product,inventory):
        try:
            warehouse= Warehouse(product,inventory)
            cls.warehouse_da.edit(warehouse)
            return True, f"warehouse {product} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls,product ):
        try:
            cls.warehouse_da.remove(product)
            return True, f"warehouse {product} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.warehouse_da.find_all()
        except Exception as e:
            return False, str(e)



