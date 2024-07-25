from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class All_login(AbstractUser):
    USER_TYPES = (
        ('agency', 'Agency'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    status = models.CharField(null=True,blank=True,max_length=10, default='pending')
    def __str__(self):
        return self.username

class Customer(models.Model):
    login_id = models.ForeignKey(All_login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(null=True,blank=True)
    dob = models.DateField()
    image = models.FileField()
    def __str__(self):
        return self.name
    
class Agency(models.Model):
    login_id = models.ForeignKey(All_login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(null=True,blank=True)
    image = models.FileField()
    document = models.FileField()
    def __str__(self):
        return self.name

class Packages(models.Model):
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    package_name =  models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    start_place = models.CharField(max_length=50)
    end_place = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    days = models.CharField(max_length=50)
    price_adult = models.IntegerField()
    price_children = models.IntegerField()
    image1 = models.FileField()
    image2 = models.FileField()
    image3 = models.FileField()
    image4 = models.FileField()
    def __str__(self):
        return self.place

class Booking(models.Model):
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    user_id =   models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_daytime =   models.DateTimeField(auto_now=True)
    booking_day = models.DateField()
    booking_amount = models.IntegerField()
    total_no = models.IntegerField()
    status = models.CharField(null=True,blank=True,max_length=10, default='pending')


class Reviews(models.Model):
     user_id =   models.ForeignKey(Customer, on_delete=models.CASCADE)
     package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
     rating = models.CharField(max_length=50)
     description = models.CharField(max_length=200)
     date = models.DateTimeField(auto_now=True)


