from django.contrib import admin
from .models import Customer,All_login,Agency,Packages,Booking,Reviews
# Register your models here.
admin.site.register(All_login)
admin.site.register(Customer)
admin.site.register(Agency)
admin.site.register(Packages)
admin.site.register(Booking)
admin.site.register(Reviews)
