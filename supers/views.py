from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request
from .models import Super
from .serializers import SuperSerializer
from super_types.models import SuperType
from rest_framework import status
from django.http import Http404

class SupersList(APIView):

    def get(self, request):
        type_param = request.query_params.get('type')
        supers = Super.objects.all()

        if type_param:
            
            supers = supers.filter(super_type__type=type_param)

        else:
            custom_response = {}
            super_types = SuperType.objects.all()
            for super_type in super_types:
                
                supers = Super.objects.filter(super_type=super_type.id)
                
                super_serializer = SuperSerializer(supers, many=True)

                custom_response[super_type.type] = (super_serializer.data)
            return Response(custom_response)

        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupersDetail(APIView):

    def get_object(self, pk):
        try:
            return Super.objects.get(pk=pk)
        except Super.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        super = self.get_object(pk=pk)
        serializer = SuperSerializer(super)
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