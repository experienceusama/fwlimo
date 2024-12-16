from rest_framework import generics
from .models import City, NewsletterSubscription, SiteReview
from .serializers import CitySerializer, ContactMessageSerializer, NewsletterSubscriptionSerializer, SiteReviewSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ContactMessageAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Thank you for your message!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class NewsletterSubscribeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = NewsletterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            # Check if email already subscribed
            email = serializer.validated_data['email']
            if NewsletterSubscription.objects.filter(email=email).exists():
                return Response({'message': 'This email is already subscribed.'}, status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response({'message': 'Thank you for subscribing to our newsletter!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SiteReviewListView(ListAPIView):
    queryset = SiteReview.objects.all()
    serializer_class = SiteReviewSerializer