from .models import User
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class ListPaginated(generics.ListAPIView):
    """
    This is paginated view
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    paginate_by = 2
    paginate_by_param = 'page_size'
    max_paginated_by = 2


class ListAll(views.APIView):
    """
    This view is according to the question asked in the problem statement
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = User.objects.all()
        serializer_context = {
            'request': request,
        }
        serialized_data = UserSerializer(
            queryset, many=True, context=serializer_context
        )
        return_data = {
            'ok': True,
            'members': serialized_data.data
        }
        return Response(return_data)
