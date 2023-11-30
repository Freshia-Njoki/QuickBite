from django.contrib import admin
from yummyapp.models import Member, Order, Pay
# Register your models here.

admin.site.register(Member)
admin.site.register(Order)
admin.site.register(Pay)