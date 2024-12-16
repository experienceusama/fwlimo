from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    

class ContactMessage(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    mobile_number = PhoneNumberField(blank=False, null=False)
    message = models.TextField()


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email
    

class SiteReview(TimeStampedModel):
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], default=1)
    title = models.CharField(max_length=255, blank=True, default="review")
    description = models.TextField(default="very good")
    name = models.CharField(max_length=255, blank=True, default="Ahmed")
    image = models.ImageField(upload_to='reviews/images/', null=True)

    def __str__(self):
        return f"Review by {self.name if self.name else 'Anonymous'}"