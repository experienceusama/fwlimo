from django.urls import path
from .views import CityListView, ContactMessageAPIView, NewsletterSubscribeAPIView, SiteReviewListView

urlpatterns = [
    path('cities/', CityListView.as_view(), name='city-list'),  # Listing cities
    path('contact/', ContactMessageAPIView.as_view(), name='contact_api'),
    path('subscribe/', NewsletterSubscribeAPIView.as_view(), name='newsletter_subscribe'),
    path('reviews/', SiteReviewListView.as_view(), name='site-review-list'),
]