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

    def create(self, validated_data):
        transaction = Transaction.objects.create(**validated_data)
        category = validated_data["category"]
        wallet = validated_data["wallet"]
        amount = validated_data["amount"]

        if category == "Income":
            wallet.balance = wallet.balance + amount
        elif category == "Debt" or category == "Expense":
            wallet.balance = wallet.balance - amount

        wallet.save()
        transaction.save()

        return transaction
