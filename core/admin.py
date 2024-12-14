from django.contrib import admin
from .models import City, ContactMessage, NewsletterSubscription

admin.site.register(City)
admin.site.register(ContactMessage)
admin.site.register(NewsletterSubscription)