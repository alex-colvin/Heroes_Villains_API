from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeSerializer
from rest_framework import status
from django.http import Http404

class SuperTypeList(APIView):

    def get(self, request):
        supertypes = SuperType.objects.all()
        serializer = SuperTypeSerializer(supertypes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SuperTypeSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperTypeDetail(APIView):

    def get_object(self, pk):
        try:
            return SuperType.objects.get(pk)
        except SuperType.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supertype = self.get_object(pk)
        serializer = SuperTypeSerializer(supertype, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        supertype = self.get_object(pk)
        serializer = SuperTypeSerializer(supertype, data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        supertype = self.get_object(pk)
        supertype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)