from django.contrib import admin
from .models.credit import Credit
from .models.debit import Debit

# Register your models here.
admin.site.register(Credit)
admin.site.register(Debit)