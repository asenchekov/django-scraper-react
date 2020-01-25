from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer

# Item Viewset
class ItemViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    # def get_queryset(self):
    #     return self.request.user.item.all()
