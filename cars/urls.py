from django.urls import path
from .views import MakeModelListView, create_reservation, CategoryListView
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register(r'', CarViewSet)

urlpatterns = [
    path('make-models/', MakeModelListView.as_view(), name='make-model-list'),
    path('reservations/create/', create_reservation, name='create-reservation'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
] + router.urls
