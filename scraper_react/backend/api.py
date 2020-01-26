from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer

# Item Viewset
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        sortby = self.request.query_params.get('sortby', None)
        if sortby is not None:
            return Item.objects.order_by(sortby)
        return Item.objects.all()
