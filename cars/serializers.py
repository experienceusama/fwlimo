from rest_framework import serializers
from .models import Car, Category, Make, Model, Reservation, CarImage
from users.models import CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name']


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']

class CarSerializer(serializers.ModelSerializer):
    # Use StringRelatedField or just return the name directly
    category = serializers.CharField(source='category.name', read_only=True)
    make = serializers.CharField(source='make.name', read_only=True)
    model = serializers.CharField(source='model.name', read_only=True)
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'category', 'make', 'model', 'model_date', 'seats', 'color', 'price', 'image', 'images']



class MakeModelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    make_model = serializers.CharField()

    class Meta:
        fields = ['id', 'make_model']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['pickup_location', 'drop_off_location', 'reservation_date', 'reservation_time', 'passengers', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile_number']

    def create(self, validated_data):
        # Create a new user
        user = CustomUser.objects.create(**validated_data)
        return user