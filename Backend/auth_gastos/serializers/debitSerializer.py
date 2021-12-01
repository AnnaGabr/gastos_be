from rest_framework import serializers
from auth_gastos.models.debit import Debit

class DebitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Debit
        fields = ["debit_Amount", "debit_Description", "debit_User", "debit_Date", "debit_User"]