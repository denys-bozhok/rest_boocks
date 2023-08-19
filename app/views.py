from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import SerializedHome
from .models import Boock

# Create your views here.

class Home(APIView):
    
    def get(self, req, *args, **kwargs):
        arg = req.META['PATH_INFO'].split('/')[-1]
        if arg:
            boock = Boock.objects.get(id=int(arg))
            serialized_boock = SerializedHome(boock).data
            print(SerializedHome(boock).data) 
            return Response(serialized_boock, status.HTTP_200_OK)
        else:
            boocks = Boock.objects.all()
            serialized_boock_list = SerializedHome(boocks, many=True).data
            print(SerializedHome(boocks, many=True).data)
            return Response(serialized_boock_list, status.HTTP_200_OK)