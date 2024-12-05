from django.urls import path
from .views import CarListView, MakeModelListView, create_reservation, CategoryListView

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),  # Listing cars
    path('make-models/', MakeModelListView.as_view(), name='make-model-list'),
    path('reservations/create/', create_reservation, name='create-reservation'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
