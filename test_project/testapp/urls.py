from django.urls import path
from .views import *

urlpatterns = [
    path('items_create', ItemCreate.as_view(), name='item-create'),
    path('items', ItemRetrieveView.as_view(), name='item-detail'),
    path('items/<int:pk>', ItemRetrieveByidView.as_view(), name='item-detail-by-id'),
    path('items_update/<int:pk>', ItemUpdateById.as_view(), name='item-update-by-id'),
    path('items_del/<int:pk>', ItemDeleteById.as_view(), name='item-delete-by-id'),
    
    
]