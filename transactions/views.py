from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework import viewsets, permissions
from knox.models import AuthToken
from knox.auth import TokenAuthentication

# Create your views here.


class TransactionViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and getting the details of a transaction """

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = Transaction.objects.filter(
            wallet__owner=self.request.user).order_by('-date')

        return queryset
