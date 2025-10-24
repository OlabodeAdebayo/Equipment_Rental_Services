from django.urls import path
from .views import EquipmentListCreateView, EquipmentDetailView

urlpatterns = [
    path('', EquipmentListCreateView.as_view(), name='equipment-list'),
    path('<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
]
