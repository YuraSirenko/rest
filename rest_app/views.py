from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CustomerSerializer, ItemSerializer, ItemHasOrderSerializer, ItemTypeSerializer, OrderSerializer, PaymentMethodSerializer, SalaryHistorySerializer, SalaryTypeSerializer, SaleSerializer, TableInRestaurantSerializer, WaiterSerializer, WaiterHasOrderSerializer
from .facade import RepositoryFacade
from rest_framework.permissions import IsAuthenticated

facade = RepositoryFacade()

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_customers()
    serializer_class = CustomerSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        customers = facade.get_all_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        customer = facade.get_customer_by_id(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_customer(pk)
        return Response(status=204)

class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_items()
    serializer_class = ItemSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        items = facade.get_all_items()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = facade.get_item_by_id(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_item(pk)
        return Response(status=204)

class ItemHasOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_item_has_orders()
    serializer_class = ItemHasOrderSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        item_has_orders = facade.get_all_item_has_orders()
        serializer = ItemHasOrderSerializer(item_has_orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item_has_order = facade.get_item_has_order_by_id(pk)
        serializer = ItemHasOrderSerializer(item_has_order)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_item_has_order(pk)
        return Response(status=204)

class ItemTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_item_types()
    serializer_class = ItemTypeSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        item_types = facade.get_all_item_types()
        serializer = ItemTypeSerializer(item_types, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item_type = facade.get_item_type_by_id(pk)
        serializer = ItemTypeSerializer(item_type)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_item_type(pk)
        return Response(status=204)

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_orders()
    serializer_class = OrderSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        orders = facade.get_all_orders()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        order = facade.get_order_by_id(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_order(pk)
        return Response(status=204)

class PaymentMethodViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_payment_methods()
    serializer_class = PaymentMethodSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        payment_methods = facade.get_all_payment_methods()
        serializer = PaymentMethodSerializer(payment_methods, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        payment_method = facade.get_payment_method_by_id(pk)
        serializer = PaymentMethodSerializer(payment_method)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_payment_method(pk)
        return Response(status=204)

class SalaryHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_salary_histories()
    serializer_class = SalaryHistorySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        salary_histories = facade.get_all_salary_histories()
        serializer = SalaryHistorySerializer(salary_histories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        salary_history = facade.get_salary_history_by_id(pk)
        serializer = SalaryHistorySerializer(salary_history)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_salary_history(pk)
        return Response(status=204)

class SalaryTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_salary_types()
    serializer_class = SalaryTypeSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        salary_types = facade.get_all_salary_types()
        serializer = SalaryTypeSerializer(salary_types, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        salary_type = facade.get_salary_type_by_id(pk)
        serializer = SalaryTypeSerializer(salary_type)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_salary_type(pk)
        return Response(status=204)

class SaleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_sales()
    serializer_class = SaleSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        sales = facade.get_all_sales()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        sale = facade.get_sale_by_id(pk)
        serializer = SaleSerializer(sale)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_sale(pk)
        return Response(status=204)

class TableInRestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_tables_in_restaurant()
    serializer_class = TableInRestaurantSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        tables_in_restaurant = facade.get_all_tables_in_restaurant()
        serializer = TableInRestaurantSerializer(tables_in_restaurant, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        table_in_restaurant = facade.get_table_in_restaurant_by_id(pk)
        serializer = TableInRestaurantSerializer(table_in_restaurant)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_table_in_restaurant(pk)
        return Response(status=204)

class WaiterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_waiters()
    serializer_class = WaiterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        waiters = facade.get_all_waiters()
        serializer = WaiterSerializer(waiters, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        waiter = facade.get_waiter_by_id(pk)
        serializer = WaiterSerializer(waiter)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_waiter(pk)
        return Response(status=204)

class WaiterHasOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_waiter_has_orders()
    serializer_class = WaiterHasOrderSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        waiter_has_orders = facade.get_all_waiter_has_orders()
        serializer = WaiterHasOrderSerializer(waiter_has_orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        waiter_has_order = facade.get_waiter_has_order_by_id(pk)
        serializer = WaiterHasOrderSerializer(waiter_has_order)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_waiter_has_order(pk)
        return Response(status=204)