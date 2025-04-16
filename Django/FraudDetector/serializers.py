from rest_framework import serializers
from .models import *


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactions
        fields = '__all__'

    def create(self, validated_data):
        return BankTransactions.objects.create(**validated_data)


class TransactionCreateSerializer(serializers.Serializer):
    pass    #TODO настроить модель


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankComplaints
        fields = '__all__'

    def create(self, validated_data):
        return BankComplaints.objects.create(**validated_data)


class ComplaintCreateSerializer(serializers.Serializer):
    pass    #TODO настроить модель
