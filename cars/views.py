from .models import Car, Category
from users.models import CustomUser
from .serializers import CarSerializer, MakeModelSerializer
from rest_framework import generics
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import City
from .serializers import UserSerializer, ReservationSerializer, CategorySerializer
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__id=category)

        return queryset
    


class MakeModelListView(generics.ListAPIView):
    serializer_class = MakeModelSerializer

    def get_queryset(self):
        # Query distinct make and model combinations with the car ID
        make_models = Car.objects.values('make__name', 'model__name', 'id').distinct()

        # Prepare a list of dictionaries with make_model and car id
        make_model_list = [
            {'id': car['id'], 'make_model': f"{car['make__name']} {car['model__name']}"}
            for car in make_models
        ]
        return make_model_list




@api_view(['POST'])
def create_reservation(request):
    """
    Accepts user data (first name, last name, email, mobile number) and reservation data
    and either creates a new user or links to an existing user based on the mobile number.
    The operation is wrapped in a transaction to ensure atomicity.
    """
    user_data = request.data.get('user')
    reservation_data = request.data.get('reservation')

    if not user_data or not reservation_data:
        return Response({'error': 'User and reservation data are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if user exists by mobile number
    mobile_number = user_data.get('mobile_number')
    
    try:
        with transaction.atomic():  # Ensure the operations are atomic
            try:
                # Check if user exists by mobile number
                user = CustomUser.objects.get(mobile_number=mobile_number)
                # Update user fields if any of the data has changed
                for attr, value in user_data.items():
                    if getattr(user, attr) != value:
                        setattr(user, attr, value)
                user.save()  # Save the updated user
            except ObjectDoesNotExist:
                # If user doesn't exist, create a new one
                user_serializer = UserSerializer(data=user_data)
                if user_serializer.is_valid():
                    user = user_serializer.save()
                else:
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Validate and create reservation
            pickup_location = reservation_data.get('pickup_location')
            drop_off_location = reservation_data.get('drop_off_location')

            try:
                pickup_city = City.objects.get(id=pickup_location)
                drop_off_city = City.objects.get(id=drop_off_location)
            except City.DoesNotExist:
                return Response({'error': 'Invalid city IDs for pickup or drop-off'}, status=status.HTTP_400_BAD_REQUEST)

            # Prepare reservation data
            reservation_data['user'] = user.id
            reservation_data['pickup_location'] = pickup_location
            reservation_data['drop_off_location'] = drop_off_location

            # Serialize reservation data and save
            reservation_serializer = ReservationSerializer(data=reservation_data)
            if reservation_serializer.is_valid():
                reservation_serializer.save()
                return Response({
                    'reservation': reservation_serializer.data
                }, status=status.HTTP_201_CREATED)
            
            # If reservation serializer is invalid, return errors
            return Response(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer