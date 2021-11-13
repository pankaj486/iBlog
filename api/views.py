from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api import serializers



class TodoAPIView(APIView):
    serializer_class = serializers.TodoSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            message = f'Your {title} and {content}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
