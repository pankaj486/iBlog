from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from todo.models import Todo



# class TodoAPIView(APIView):
#     serializer_class = serializers.TodoSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')
#             message = f'Your {title} and {content}'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status = status.HTTP_400_BAD_REQUEST
#             )

@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        'List': 'This is fuction based view',
        'Detail': 'Only the show data',
    }
    return Response(api_urls)

@api_view(["GET"])
def todoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def todoDetail(request, id):
    todo = Todo.objects.get(pk=id)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(["DELETE"])
def todoDelete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return Response("Todo is successfully deleted.")
