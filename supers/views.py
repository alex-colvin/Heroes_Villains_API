from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperSerializer
from rest_framework import status
from django.http import Http404

class SupersList(APIView):

    def get(self, request):
        supers = self.object.all()
        serializer = SuperSerializer
