from api.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserEmailUpdate(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self):
        try:
            email = self.request.data.get('email')
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        print(repr(serializer.data))

        return Response(serializer.data)
    def put(self, request, format=None):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



