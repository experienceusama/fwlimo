from django.contrib import admin
from .models import City, ContactMessage, NewsletterSubscription, SiteReview

admin.site.register(City)
admin.site.register(ContactMessage)
admin.site.register(NewsletterSubscription)
admin.site.register(SiteReview)