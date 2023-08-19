from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import SerializedReview
from .models import Review

# Create your views here.

class Reviews(APIView):
    
    def get(self, req):

        reviews = Review.objects.all()
        serialized_boock_list = SerializedReview(reviews, many=True).data
        print(SerializedReview(reviews, many=True).data)
        return Response(serialized_boock_list, status.HTTP_200_OK)
