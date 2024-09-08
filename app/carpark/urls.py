"""
URL mappings for the car park API.
"""
from django.urls import path
from .views import CarParkViewSet

app_name = 'carpark'

urlpatterns = [
    path('create/', CarParkViewSet.as_view({'post': 'create'}), name='create'),
    path('<int:pk>/', CarParkViewSet.as_view({'get': 'retrieve'}), name='detail'),
    path('', CarParkViewSet.as_view({'get': 'list'}), name='list'),
    path('update/<int:pk>/', CarParkViewSet.as_view({'put': 'update'}), name='update'),
    path('delete/<int:pk>/', CarParkViewSet.as_view({'delete': 'destroy'}), name='delete'),
]
