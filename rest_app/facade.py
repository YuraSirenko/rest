from rest_app.repositories.customer_repository import CustomerRepository
from rest_app.repositories.item_repository import ItemRepository
from rest_app.repositories.item_has_order_repository import ItemHasOrderRepository
from rest_app.repositories.item_type_repository import ItemTypeRepository
from rest_app.repositories.order_repository import OrderRepository
from rest_app.repositories.payment_method_repository import PaymentMethodRepository
from rest_app.repositories.salary_history_repository import SalaryHistoryRepository
from rest_app.repositories.salary_type_repository import SalaryTypeRepository
from rest_app.repositories.sale_repository import SaleRepository
from rest_app.repositories.table_in_restaurant_repository import TableInRestaurantRepository
from rest_app.repositories.waiter_repository import WaiterRepository
from rest_app.repositories.waiter_has_order_repository import WaiterHasOrderRepository
class RepositoryFacade:
    def __init__(self):
        self.customer_repository = CustomerRepository()
        self.item_repository = ItemRepository()
        self.item_has_order_repository = ItemHasOrderRepository()
        self.item_type_repository = ItemTypeRepository()
        self.order_repository = OrderRepository()
        self.payment_method_repository = PaymentMethodRepository()
        self.salary_history_repository = SalaryHistoryRepository()
        self.salary_type_repository = SalaryTypeRepository()
        self.sale_repository = SaleRepository()
        self.table_in_restaurant_repository = TableInRestaurantRepository()
        self.waiter_repository = WaiterRepository()
        self.waiter_has_order_repository = WaiterHasOrderRepository()

    def get_all_customers(self):
        return self.customer_repository.get_all()

    def get_customer_by_id(self, id):
        return self.customer_repository.get_by_id(id)

    def delete_customer(self, id):
        return self.customer_repository.delete(id)

    def get_all_items(self):
        return self.item_repository.get_all()

    def get_item_by_id(self, id):
        return self.item_repository.get_by_id(id)

    def delete_item(self, id):
        return self.item_repository.delete(id)

    def get_all_item_has_orders(self):
        return self.item_has_order_repository.get_all()

    def get_item_has_order_by_id(self, id):
        return self.item_has_order_repository.get_by_id(id)

    def delete_item_has_order(self, id):
        return self.item_has_order_repository.delete(id)

    def get_all_item_types(self):
        return self.item_type_repository.get_all()

    def get_item_type_by_id(self, id):
        return self.item_type_repository.get_by_id(id)

    def delete_item_type(self, id):
        return self.item_type_repository.delete(id)

    def get_all_orders(self):
        return self.order_repository.get_all()

    def get_order_by_id(self, id):
        return self.order_repository.get_by_id(id)

    def delete_order(self, id):
        return self.order_repository.delete(id)

    def get_all_payment_methods(self):
        return self.payment_method_repository.get_all()

    def get_payment_method_by_id(self, id):
        return self.payment_method_repository.get_by_id(id)

    def delete_payment_method(self, id):
        return self.payment_method_repository.delete(id)

    def get_all_salary_histories(self):
        return self.salary_history_repository.get_all()

    def get_salary_history_by_id(self, id):
        return self.salary_history_repository.get_by_id(id)

    def delete_salary_history(self, id):
        return self.salary_history_repository.delete(id)

    def get_all_salary_types(self):
        return self.salary_type_repository.get_all()

    def get_salary_type_by_id(self, id):
        return self.salary_type_repository.get_by_id(id)

    def delete_salary_type(self, id):
        return self.salary_type_repository.delete(id)

    def get_all_sales(self):
        return self.sale_repository.get_all()

    def get_sale_by_id(self, id):
        return self.sale_repository.get_by_id(id)

    def delete_sale(self, id):
        return self.sale_repository.delete(id)

    def get_all_tables_in_restaurant(self):
        return self.table_in_restaurant_repository.get_all()

    def get_table_in_restaurant_by_id(self, id):
        return self.table_in_restaurant_repository.get_by_id(id)

    def delete_table_in_restaurant(self, id):
        return self.table_in_restaurant_repository.delete(id)

    def get_all_waiters(self):
        return self.waiter_repository.get_all()

    def get_waiter_by_id(self, id):
        return self.waiter_repository.get_by_id(id)

    def delete_waiter(self, id):
        return self.waiter_repository.delete(id)

    def get_all_waiter_has_orders(self):
        return self.waiter_has_order_repository.get_all()

    def get_waiter_has_order_by_id(self, id):
        return self.waiter_has_order_repository.get_by_id(id)

    def delete_waiter_has_order(self, id):
        return self.waiter_has_order_repository.delete(id)