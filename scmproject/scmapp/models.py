from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.core.validators import RegexValidator


    # other fields and methods for the user model
class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=50,blank=False)
    gender_choices = ( ("M","Male") , ("F","Female")  , ("Others","Prefer not to say")  )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth=models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    password = models.CharField(
        max_length=128,
        validators=[
            RegexValidator(
                regex=password_regex,
                message="Password must contain at least 8 characters, with at least one letter, one number, and one special character",
                code="invalid_password"
            )
        ]
    )
    location = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=10,blank=False,unique=True)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "registration_table"

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100,default=False)
    seller = models.CharField(max_length=100,default=False)
    quantity=models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    class Meta:
        db_table = "product_table"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)



    class Meta:
        db_table = "Customer_table"

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    delivery_address = models.CharField(max_length=200)
    payment_terms = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "Order_table"




class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"



