from rest_app_2.models import ItemHasOrder

class ItemHasOrderService:
    @staticmethod
    def get_by_order_and_item(order, item):
        try:
            return ItemHasOrder.objects.get(order=order, item=item)
        except ItemHasOrder.DoesNotExist:
            return None