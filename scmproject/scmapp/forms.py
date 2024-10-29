from django import forms
from django.contrib.auth.models import User

from .models import Registration, Product, Customer, Order, Admin, Supplier, Seller


class DateInput(forms.DateInput):
    input_type = "date"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}



class ProductForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(),to_field_name='name')
    seller = forms.ModelChoiceField(queryset=Seller.objects.all(),to_field_name='')
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'supplier','seller','quantity','image']



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'address', 'phone']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity', 'delivery_address', 'payment_terms']



class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'phone_number', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'phone_number', 'email']
