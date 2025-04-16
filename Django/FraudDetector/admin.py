from django.contrib import admin
from .models import *

admin.site.register(BankClient)
admin.site.register(BankComplaint)
admin.site.register(BankTransaction)
