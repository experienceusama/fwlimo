from rest_framework import serializers
from .models import City, ContactMessage, NewsletterSubscription
from django.contrib.auth import get_user_model


User = get_user_model()


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'message']

    def create(self, validated_data):
        mobile_number = validated_data.get('mobile_number')
        user = User.objects.filter(mobile_number=mobile_number).first()
        validated_data['user'] = user
        return ContactMessage.objects.create(**validated_data)
    

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def create(self, validated_data):
        email = validated_data['email']
        user = User.objects.filter(email=email).first()
        return NewsletterSubscription.objects.create(email=email, user=user)