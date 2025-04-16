from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
import requests


# Импортируем переменные телеграм бота
# from Bot.vars import bot_token, chat_id

# Задаём переменную сообщения от бота
# message = ''
# Отправляем сообщение через Telegram API
# requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')


class TransactionsView(APIView):
    def get(self, request):
        txns = BankTransaction.objects.all()
        serialized = TransactionSerializer(txns, many=True)
        return Response(serialized.data)


class SingleTransactionView(APIView):
    def get(self, request, id):
        txn = BankTransaction.objects.get(id=id)
        serialized = TransactionSerializer(txn)
        return Response(serialized.data)


class ComplaintsView(APIView):
    def get(self, request):
        complains = BankComplaint.objects.all()
        serialized = ComplaintSerializer(complains, many=True)
        return Response(serialized.data)


class SingleComplaintView(APIView):
    def get(self, request, user_id):
        complain = BankComplaint.objects.get(user_id)
        serialized = ComplaintSerializer(complain)
        return Response(serialized.data)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
