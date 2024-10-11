from django.shortcuts import render
from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from ledger.models import TacoLedger
from user.serializers import UserTransactionSerializer
from django.db.models import Q
from datetime import datetime


class MEView(APIView):
    renderer_classes = [JSONRenderer]
    serializer_class = UserSerializer

    def get(self, request):
        """
        Return user details
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserTransactionView(viewsets.ModelViewSet):

    serializer_class = UserTransactionSerializer

    def get_user(self):
        return User.objects.filter(id=self.kwargs.get('pk')).first()

    def get_queryset(self, start_date, end_date):
        user = self.get_user()
        user_id = user.unique_id
        query = Q(receiver=user_id) | Q(giver=user_id)
        query &= Q(timestamp__gte=datetime.strptime(start_date, '%Y-%m-%d'))
        query &= Q(timestamp__lte=datetime.strptime(end_date, '%Y-%m-%d'))
        return TacoLedger.objects.filter(query)

    def list(self, request, pk):
        ser = UserTransactionSerializer(
            data={
                'start_date': request.query_params.get('start_date'),
                'end_date': request.query_params.get('end_date')
            }
        )
        if ser.is_valid(raise_exception=True):
            transactions = self.get_queryset(
                ser.validated_data.get('start_date'),
                ser.validated_data.get('end_date')
            )
            formatted_transactions = [{
                'amount': t.amount,
                'date': t.timestamp,
                'giver': self.parse_user_id(t.giver),
                'receiver': self.parse_user_id(t.receiver)}
                for t in transactions
            ]
            return Response(status=200, data={'transactions': formatted_transactions})
        return Response(status=400)
    
    def parse_user_id(self, user_id):
        """
        Figure out the name of the user based on the unique ID.

        Args:
            user_id (str): user's user.unique_id

        Returns:
            str: First and last name of user else 'unknown user'
        """
        user = User.objects.filter(unique_id=user_id).first()
        if user:
            return f'{user.first_name} {user.last_name}'
        return 'unknown user'
