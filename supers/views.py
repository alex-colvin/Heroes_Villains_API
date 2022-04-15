from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer
from rest_framework import status
from django.http import Http404

class SupersList(APIView):

    def get(self, request):
        supers = self.object.all()
        serializer = SuperSerializer(supers, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperDetail(APIView):

    def get_object(self, pk):
        try:
            return Super.objects.get(pk)
        except Super.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        super = self.get_object(pk)
        serializer = SuperSerializer(super, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        super = self.get_object(pk)
        serializer = SuperSerializer(super, data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        super = self.get_object(pk)
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)