from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """ Serializes Transaction """

    class Meta:
        model = Transaction
        fields = [
            "id",
            "wallet",
            "category",
            "amount",
            "date",
            "note",
        ]