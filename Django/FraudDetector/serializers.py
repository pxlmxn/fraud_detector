from rest_framework import serializers
from .models import *


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransaction
        fields = '__all__'

    def create(self, validated_data):
        return BankTransaction.objects.create(**validated_data)


class TransactionCreateSerializer(serializers.Serializer):
    pass    #TODO настроить модель


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankComplaint
        fields = '__all__'

    def create(self, validated_data):
        return BankComplaint.objects.create(**validated_data)


class ComplaintCreateSerializer(serializers.Serializer):
    pass    #TODO настроить модель
