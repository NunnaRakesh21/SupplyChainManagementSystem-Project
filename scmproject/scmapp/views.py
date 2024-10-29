from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import RegistrationForm, ProductForm, CustomerForm, OrderForm, SupplierForm, SellerForm
from .models import Registration, Product, Customer, Order, Admin,Supplier


def indexfunction(request):
    return render(request,"index.html")


def registration(request):
    form=RegistrationForm()

    if request.method=="POST":
        formdata=RegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Thank you for registering. You can now log in to your account."
            return render(request,"registration.html",{"form": form,"msg":msg})
        else:
            msg="Password must contain at least 8 characters, with at least one letter, one number, and one special character"
            return render(request, "registration.html", {"form": form, "msg": msg})
    return render(request,"registration.html",{"form":form})

def login(request):
    return render(request,"login.html")

def checkuserlogin(request):
    uname=request.POST["username"]
    pwd=request.POST["pswrd"]

    flag=Registration.objects.filter( Q(username=uname) & Q(password=pwd))
    print(flag)

    if flag:
        user=Registration.objects.get(username=uname)
        print(user)
        print(user.id,user.fullname,user.username) #other fields also
        request.session["uname"]=user.username
        msg="A notification will be sent to email"
        return render(request,"base.html",{"uname":user.username,"msg":msg})
    else:
        msg="Invalid username or password"
        return render(request,"login.html",{"msg":msg})

def home(request):
    return render(request,"home.html")

def services(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")

def logout(request):
    return render(request,"login.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg="Product added sucesfully"
            return render(request,"add_product.html",{"msg":msg})
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def customer_list(request):
    customers = Registration.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})



def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})



def basic(request):
    return render(request,"base.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminpurpose.html", {"auname": admin.username})
    else:
        msg = "Invalid username or password"
        return render(request, "adminlogin.html", {"msg": msg})

def adminpurpose(request):
    return render(request,"adminpurpose.html")

def adminlogout(request):
    return render(request,"adminlogin.html")

def createsupplier(request):
    form=SupplierForm()

    if request.method == "POST":
        formdata = SupplierForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "Successfully Added Supplier"
            return render(request, "createsupplier.html", {"form": form, "msg": msg})
        else:
            msg = "Failed to Add supplier"
            return render(request, "createsupplier.html", {"form": form, "msg": msg})
    return render(request, "createsupplier.html", {"form": form})

def supplierlogin(request):
    return render(request,"supplierlogin.html")

def supplieruserlogin(request):
    uname=request.POST["mailid"]
    pwd=request.POST["pswrd"]

    flag=Supplier.objects.filter( Q(email=uname) & Q(password=pwd))
    print(flag)

    if flag:
        user=Supplier.objects.get(email=uname)
        request.session["uname"]=user.email
        return render(request,"supplierpurpose.html",{"uname":user.email})
    else:
        msg="Invalid username or password"
        return render(request,"supplierlogin.html",{"msg":msg})

def supplierlogout(request):
    return render(request,"supplierlogin.html")

def deletecustomer(request,uid):
    Registration.objects.filter(id=uid).delete()
    return redirect("customer_list")

def createseller(request):
    form=SellerForm()

    if request.method == "POST":
        formdata = SellerForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "Successfully Added Seller"
            return render(request, "createseller.html", {"form": form, "msg": msg})
        else:
            msg = "Failed to Add seller"
            return render(request, "createseller.html", {"form": form, "msg": msg})
    return render(request, "createseller.html", {"form": form})