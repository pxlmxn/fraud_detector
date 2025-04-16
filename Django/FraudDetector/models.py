from django.db import models
from django.db.models import DO_NOTHING


class BankClient(models.Model):
    user_id = models.CharField()
    account = models.CharField()
    phone = models.CharField()
    fio = models.CharField()

    def __str__(self):
        return str(self.fio)


class MobileClient(models.Model):
    client_id = models.CharField()
    phone = models.CharField()
    fio = models.CharField()
    address = models.CharField()


class BankComplaint(models.Model):
    event_date = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.text


class BankTransaction(models.Model):
    event_date = models.DateTimeField(auto_now=True)
    account_out = models.CharField(max_length=50)
    account_in = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return str(self.id)


class EcosystemMapping(models.Model):
    bank = models.CharField(max_length=50)
    mobile_user_id = models.CharField(max_length=50)
    market_place_user_id = models.CharField(max_length=50)


class MarketPlaceDelivery(models.Model):
    event_date = models.DateTimeField(auto_now=True)
    market_place_user_id = models.CharField(max_length=50)


class MobileBuild(models.Model):
    event_date = models.DateTimeField(auto_now=True)
    from_call = models.CharField(max_length=50)
    to_call = models.CharField(max_length=50)
    duration_sec = models.IntegerField()

